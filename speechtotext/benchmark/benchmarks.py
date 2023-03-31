"""Module for benchmarks of speechtotext.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.datasets import Dataset
	from speechtotext.benchmark.benchmarks import *
 
	# Settings
	number_of_samples = 10
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
	wb = WhisperBenchmark()
	wAPIb = WhisperAPIBenchmark()
	benchmark_dataset = dataset_RDH
	benchmark_list: list[Benchmark] = [wb, wAPIb]
 
	# Run benchmarks
	results = run_benchmarks(benchmark_list, benchmark_dataset, number_of_samples)
"""

from abc import ABC, abstractmethod
import pandas as pd

from speechtotext.model.modelWrapper import ModelWrapper
from speechtotext.model.whisperWrapper import WhisperVersion, WhisperWrapper, WhisperAPIWrapper, WhisperAPIVersion
from speechtotext.datasets import Dataset
from speechtotext.functions import multidispatch, join_benchmark_results, separate_benchmark_results_by_model, DEFAULT_HTML_TITLE, DEFAULT_CSV_NAME, DEFAULT_CSV_NAME, DEFAULT_REPORTS_FOLDER


class Benchmark(ABC):
	"""Benchmark is used to test/validate an model.
	Parent class for all benchmark classes. 

	Attributes:
			BENCHMARK_SAMPLES (SampleDataset): Dataset with just samples that is shared for the child classes.
			DATASET (Dataset): Dataset that is shared for the child classes.

	"""
	BENCHMARK_SAMPLES: Dataset = None
	DATASET: Dataset = None

	def __init__(self, with_cleaning=True):
		"""Create benchmark object.

		Args:
				with_cleaning (bool, optional): Clean . Defaults to True.
		"""
		self.__with_cleaning = with_cleaning
		self.models = self.create_models()

	def save_to_csv(self, save_name: str):
		"""save outputs of benchmark to csv.

		Args:
				save_name (str): filename of output.
		"""
		df = self.convert_to_pandas()
		df.to_csv(save_name, index=False)

	def convert_to_pandas(self) -> pd.core.frame.DataFrame:
		"""convert metrics to dataframe.

		Returns:
				pd.core.frame.DataFrame: pandas dataframe.
		"""
		column_names = ["model_name", "audio_ID",
						"reference", "wer", "mer",  "wil", "wip", "cer"]
		df = pd.DataFrame(columns=column_names)

		for model, metrics in zip(self.models, self.metrics):
			model_name = f"{self.MODEL_BASE}_{model.model_version.value}"
			for metric in metrics:

				new_row = pd.Series([model_name, metric.audio_id, metric.reference, metric.wer,
									 metric.mer,  metric.wil, metric.wip, metric.cer], index=column_names)
				df = pd.concat([df, new_row.to_frame().T], ignore_index=True)

		return df

	def __call__(self, number_of_samples: int, with_cleaning=True):
		"""Benchmark n samples.

		Args:
				number_of_samples (int): number of random samples.
				with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.
		"""
		self.metrics = []
		Benchmark.update_samples(number_of_samples)

		for model in self.models:
			print(
				f"benchmark for model {model.model_version} with dataset {self.BENCHMARK_SAMPLES.name}")
			try:
				self.metrics.append(model.benchmark_samples(
					self.BENCHMARK_SAMPLES, with_cleaning))
			except Exception as e:
				print(e)

	@abstractmethod
	def create_models(self) -> list[ModelWrapper]:
		"""Creates an list of ModelWrappers.

		Returns:
				list[ModelWrapper]: list of model wrappers.
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
			if number_of_samples is cls.BENCHMARK_SAMPLES.number_of_samples():
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

def run_benchmarks(benchmark_list: list[Benchmark], benchmark_dataset:Dataset, number_of_samples:int) -> list[pd.core.frame.DataFrame]:
	"""Run al benchmarks out of list.

	Args:
		benchmark_list (list[Benchmark]): List of benchmarks to run.
		dataset (Dataset): Dataset to use for benchmark.
		number_of_samples (int): Number of samples used in benchmark.
	""" 
	results: list[pd.core.frame.DataFrame] = []
	Benchmark.set_dataset(benchmark_dataset)
	
	for index, benchmark in enumerate(benchmark_list):
		benchmark(number_of_samples)
		results.append( benchmark.convert_to_pandas())
	return results