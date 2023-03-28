#!/usr/bin/env python
from speechtotext.models.modelWrapper import ModelWrapper
from speechtotext.models.whisperWrapper import WhisperVersion, WhisperWrapper, WhisperAPIWrapper, WhisperAPIVersion
from speechtotext.datasets import Dataset
from abc import ABC, abstractmethod
import pandas as pd

class Benchmark(ABC):
 
	BENCHMARK_SAMPLES = None
	def __init__(self, dataset:Dataset,  with_cleaning=True):
		"""Create benchmark object.

		Args:
			dataset (Dataset): Dataset to test.
			with_cleaning (bool, optional): Clean . Defaults to True.
		"""     
		self.dataset = dataset
		self.__with_cleaning = with_cleaning
		self.models = self.create_models()
  
	def save_to_csv(self, save_name:str):
		"""save outputs of benchmark to csv.

		Args:
			save_name (str): filename of output.
		"""     
		df = self.convert_to_pandas()
		df.to_csv(save_name, index=False)

	def convert_to_pandas(self) ->  pd.core.frame.DataFrame:
		"""convert metrics to dataframe.

		Returns:
			pd.core.frame.DataFrame: pandas dataframe.
		"""		
		column_names = ["model_name", "audio_ID", "hypothesis", "wer", "mer",  "wil", "wip", "cer"]
		df  = pd.DataFrame(columns=column_names)

		for model, metrics in zip(self.models, self.metrics):
			model_name = f"{self.MODEL_BASE}_{model.model_version.value}"
			for metric in metrics:
				
				new_row = pd.Series([model_name, metric.audio_id, metric.hypothesis, metric.wer, 
						 				metric.mer,  metric.wil, metric.wip, metric.cer]
									, index = column_names)
				df = pd.concat([df, new_row.to_frame().T], ignore_index=True)

		return df

	def __call__(self, number_of_samples:int, with_cleaning=True):
		"""Benchmark n samples.

		Args:
			number_of_samples (int): number of random samples.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.
		"""     
		self.metrics = []
		if Benchmark.BENCHMARK_SAMPLES ==None:
			Benchmark.BENCHMARK_SAMPLES = self.dataset.get_n_samples(number_of_samples)

		for model in self.models:
			print(f"benchmark for model {model.model_version} with dataset {self.dataset.name}")
			try:
				self.metrics.append(model.benchmark_samples(Benchmark.BENCHMARK_SAMPLES, with_cleaning))
			except Exception as e:
				print(e)
	
	@abstractmethod
	def create_models(self) -> list[ModelWrapper]:
		"""Creates an list of ModelWrappers.

		Returns:
			list[ModelWrapper]: list of model wrappers.
		"""     
		pass

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