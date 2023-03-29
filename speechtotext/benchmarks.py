"""Module for benchmarks of speechtotext.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.datasets import Dataset
	from speechtotext.benchmarks import *
 
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
"""

from abc import ABC, abstractmethod
import pandas as pd
from datetime import datetime
from ydata_profiling import ProfileReport, compare

from speechtotext.models.modelWrapper import ModelWrapper
from speechtotext.models.whisperWrapper import WhisperVersion, WhisperWrapper, WhisperAPIWrapper, WhisperAPIVersion
from speechtotext.datasets import Dataset
from speechtotext.functions import multidispatch

DEFAULT_CSV_NAME = f"Benchmark_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
DEFAULT_HTML_NAME = f"Benchmark_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
DEFAULT_HTML_TITLE = f"Benchmark results of {datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"


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
						"hypothesis", "wer", "mer",  "wil", "wip", "cer"]
		df = pd.DataFrame(columns=column_names)

		for model, metrics in zip(self.models, self.metrics):
			model_name = f"{self.MODEL_BASE}_{model.model_version.value}"
			for metric in metrics:

				new_row = pd.Series([model_name, metric.audio_id, metric.hypothesis, metric.wer,
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


class WhisperBenchmark(Benchmark):
	"""Benchmark for local whisper models.
	"""
	MODEL_BASE = "Whisper"

	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in WhisperVersion:
			models.append(WhisperWrapper(version))
		return models


class WhisperAPIBenchmark(Benchmark):
	"""Benchmark for API whisper models.
	"""
	MODEL_BASE = "WhisperAPI"

	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in WhisperAPIVersion:
			models.append(WhisperAPIWrapper(version))
		return models


def join_benchmark_results(results: list[pd.core.frame.DataFrame], set_index=True) -> pd.core.frame.DataFrame:
	"""Join Benchmark results.

	Args:
			results (list[pd.core.frame.DataFrame]): results of benchmarks.
			set_index (bool, optional): Set True if ["model_name", "audio_ID"] can be set as index. Defaults to True.

	Returns:
			pd.core.frame.DataFrame: Dataframe with results of all benchmarks.
	"""
	df = pd.concat(results)
	if set_index:
		df = df.set_index(["model_name", "audio_ID"])
	return df

def separate_benchmark_results_by_model(dataframe: pd.core.frame.DataFrame) -> dict[str, pd.core.frame.DataFrame]:
	"""Seperate benchmark results for each model.

	Args:
			dataframe pd.core.frame.DataFrame: Dataframe with results of all benchmarks.

	Returns:
			(list[pd.core.frame.DataFrame]): results of benchmarks. 
	"""
	
	model_names = dataframe["model_name"].unique()

	DataFrameDict = {elem : pd.DataFrame() for elem in model_names}

	for key in DataFrameDict.keys():
		df = dataframe[:][dataframe["model_name"] == key]
		df = df.set_index("audio_ID")
		del df['model_name']
		DataFrameDict[key] = df
	
	return DataFrameDict

def benchmark_results_to_csv(results: list[pd.core.frame.DataFrame], save_name:str=DEFAULT_CSV_NAME):
	"""Creates csv from benchmark results.
	
	Args:
		results (list[pd.core.frame.DataFrame]): List of results from benchmarks.
		save_name (str, optional): filename of output. Defaults to DEFAULT_CSV_NAME.
	"""  
	df = pd.concat(results)
	df.to_csv(save_name, index=False)
 
def benchmark_results_to_html(dict_results: dict[str, pd.core.frame.DataFrame], title:str = DEFAULT_HTML_TITLE, save_name: str = DEFAULT_HTML_NAME):
	"""Saves benchmark results to html overview.

	Args:
		results (list[pd.core.frame.DataFrame]): List of results from benchmarks.
		title (str, optional): Title on the report. Defaults to DEFAULT_HTML_TITLE.
		save_name (str, optional): filename of the output. Defaults to DEFAULT_HTML_NAME.
	"""    
	reports = []
	for _, (key, df) in enumerate(dict_results.items()):
		print(key, df.columns)
		raport = ProfileReport(df, title=key)
		raport.to_file(f"benchmark_results_{key}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html")
		reports.append(raport)
	
	# comparison_report = compare(reports[0:max])
	# statistics = comparison_report.get_description()
	# comparison_report.to_file(save_name)
 
 
def save_benchmark_results(results: list[pd.core.frame.DataFrame]):
	"""Save benchmark results to csv and html.

	Args:
		results (list[pd.core.frame.DataFrame]): List of results.
	"""
	df = join_benchmark_results(results, set_index=False)
	dict_of_dfs = separate_benchmark_results_by_model(df)
	benchmark_results_to_html(dict_of_dfs)
