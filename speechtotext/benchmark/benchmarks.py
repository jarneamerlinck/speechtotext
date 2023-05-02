"""Module for benchmarks of speechtotext.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.datasets import Dataset
	from speechtotext.benchmark.benchmarks import *
 
	# Settings
	number_of_samples = 10
	report_name = "report name"
	dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
	Benchmark.set_dataset(dataset)

	# Create benchmark
	wb = WhisperBenchmark()
 
	# Run benchmark
	wb(number_of_samples)
	
	# Convert metrics to pandas dataframe
	df = wb.convert_to_pandas()
	print(df)
 
	# Save metrics to csv (saves with datetime in name)
	benchmark_results_to_csv([wb])
 
	# Run benchmarks
 	## Settings
	number_of_samples = 5
	benchmark_dataset = dataset_RDH
	benchmark_class_list: list[Benchmark] = [WhisperBenchmark, WhisperAPIBenchmark]
 
	# Run benchmarks
	results = run_benchmarks(benchmark_class_list, benchmark_dataset, number_of_samples, report_name)
"""

from abc import ABC, abstractmethod
import pandas as pd

from speechtotext.model.modelWrapper import ModelWrapper
from speechtotext.datasets import Dataset
from speechtotext.functions import multidispatch, join_benchmark_results, save_folder_name
from speechtotext.metric.metrics import Metrics


class Benchmark(ABC):
	"""Benchmark is used to test/validate an model.
	Parent class for all benchmark classes. 
	"""
	BENCHMARK_SAMPLES: Dataset = None
	"""Dataset: Dataset samples.
	"""
	DATASET: Dataset = None
	"""Dataset: Original dataset.
	"""
	ERROR_LIST: list[pd.core.frame.DataFrame] = []
	"""list[pd.core.frame.DataFrame]: List of errors.
	"""

	def __init__(self, with_cleaning=True):
		"""Create benchmark object.

		Args:
				with_cleaning (bool, optional): Clean. Defaults to True.
		"""
		self.__with_cleaning = with_cleaning
		self.models = self.create_models()

	def save_to_csv(self, save_name: str):
		"""Save outputs of benchmark to csv.

		Args:
				save_name (str): Filename of output.
		"""
		df = self.convert_to_pandas()
		df.to_csv(save_name, index=False)

	def convert_to_pandas(self) -> pd.core.frame.DataFrame:
		"""Convert metrics to dataframe.

		Returns:
				pd.core.frame.DataFrame: Pandas dataframe.
		"""
		
		# column_names = ["model_name", "audio_ID","dataset", "duration",
		# 				"reference", "wer", "mer",  "wil", "wip", "cer"]
		first_column_names = ["model_name", "audio_ID","dataset", "reference", "hypothesis"]
		metric_column_names = Metrics.get_all_metric_names()
		column_names = first_column_names + metric_column_names
		
		df = pd.DataFrame(columns=column_names)

		for model, metrics in zip(self.models, self.metrics):
			model_name = f"{self.MODEL_BASE}_{model.model_version.value}"
			for metric in metrics:
	
				new_row = pd.Series([model_name, metric.audio_id, self.BENCHMARK_SAMPLES.name, metric.reference, metric.hypothesis] + 
                    [vars(metric)[x] for x in metric_column_names]
                    	, index=column_names)
				df = pd.concat([df, new_row.to_frame().T], ignore_index=True)

		return df

	def __call__(self, number_of_samples: int, with_cleaning=True):
		"""Benchmark n samples.benchmark_results_to_csv

		Args:
			number_of_samples (int): Number of samples to benchmark.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.
		"""     
		self.metrics = []
		column_names_errors = ["model_name", "audio_ID","dataset","reference", "message"]
		df_errors = pd.DataFrame(columns=column_names_errors)

		Benchmark.update_samples(number_of_samples)

		for model in self.models:
			print(
				f"benchmark for model {model.model_version} with dataset {self.BENCHMARK_SAMPLES.name}")
			model_name = f"{self.MODEL_BASE}_{model.model_version.value}"
			try:
				self.metrics.append(model.benchmark_samples(
					self.BENCHMARK_SAMPLES, with_cleaning))
			except Exception as e:
				print(e)
			
			if model.model_errors.shape[0] != 0:
				model.model_errors["model_name"] = model_name
				model.model_errors = model.model_errors[column_names_errors]
				df_errors = pd.concat([df_errors, model.model_errors])

		self.df_errors = df_errors
  
	@abstractmethod
	def create_models(self) -> list[ModelWrapper]:
		"""Creates an list of ModelWrappers.

		Returns:
				list[ModelWrapper]: List of model wrappers.
		"""
		pass

	@classmethod
	def set_dataset(cls, dataset: Dataset):
		"""Set dataset for Benchmark class.

		Args:
				dataset (Dataset): Dataset to use with benchmark.
		"""
		cls.DATASET = dataset

	@classmethod
	@multidispatch(int)
	def update_samples(cls, number_of_samples: int):
		"""Update the sample dataset.

		Args:
				number_of_samples (int): Number of samples.
		"""
		if cls.BENCHMARK_SAMPLES is not None:
			if number_of_samples is cls.BENCHMARK_SAMPLES.number_of_samples() and cls.BENCHMARK_SAMPLES.name == cls.DATASET.name:
				return None
		cls.BENCHMARK_SAMPLES = cls.DATASET.get_n_samples(number_of_samples)

	@classmethod
	@multidispatch(Dataset, int)
	def update_samples(cls, new_dataset: Dataset, number_of_samples: int):
		"""Update the sample dataset.

		Args:
				new_dataset (Dataset): Full dataset.
				number_of_samples (int): Number of samples.
		"""
		if new_dataset.name is not cls.DATASET.name:
			cls.DATASET = new_dataset
		cls.update_samples(number_of_samples)

def run_benchmarks(benchmark_class_list: list[Benchmark], benchmark_dataset:Dataset, number_of_samples:int, report_name:str) -> list[pd.core.frame.DataFrame]:
	"""Run al benchmarks out of list.

	Args:
		benchmark_list (list[Benchmark]): List of benchmark classes to run.
		dataset (Dataset): Dataset to use for benchmark.
		number_of_samples (int): Number of samples used in benchmark.
		report_name (str): Name of report. To save the errors to.
	""" 
	results: list[pd.core.frame.DataFrame] = []
	errors: list[pd.core.frame.DataFrame] = []
	Benchmark.DATASET =  benchmark_dataset
	
	for index, benchmark_class in enumerate(benchmark_class_list):
		benchmark = benchmark_class()

		benchmark(number_of_samples)
		results.append(benchmark.convert_to_pandas())
		errors.append(benchmark.df_errors)

	Benchmark.ERROR_LIST = Benchmark.ERROR_LIST + errors
	folder = save_folder_name(report_name)
	df_error = join_benchmark_results(errors, set_index=False)
	df_error.to_csv(f"{folder}/errors_{benchmark_dataset.name}.csv", index=False)
	
	print(f"Number of errors logged to .csv file: {df_error.shape[0]}")
	return results