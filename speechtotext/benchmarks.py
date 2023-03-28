#!/usr/bin/env python
from typing_extensions import override
from speechtotext.functions import string_cleaning 
from speechtotext.models.modelWrapper import ModelWrapper
from speechtotext.models.whisperWrapper import WhisperVersion, WhisperWrapper
from speechtotext.datasets import Dataset
from abc import ABC, abstractmethod
import pandas as pd

class Benchmark(ABC):
 
	def __init__(self, dataset:Dataset,  with_cleaning=True):
		self.dataset = dataset
		self.__with_cleaning = with_cleaning
		self.models = self.create_models()
  
	def save_to_csv(self):
		pass

	def convert_to_pandas(self):
		pass

	def __call__(self, number_of_samples:int):
		self.metrics = []
		for model in self.models:
			print(f"benchmark for model {model.model_version} with dataset {self.dataset}")
			try:
				self.metrics.append(model.benchmark_n_samples(self.dataset, number_of_samples))
			except Exception as e:
				print(e)
	
	@abstractmethod
	def create_models(self) -> list[ModelWrapper]:
		"""Creates an list of ModelWrappers

		Returns:
			list[ModelWrapper]: list of model wrappers
		"""     
		pass

class WhisperBenchmark(Benchmark):
	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in WhisperVersion:
			models.append(WhisperWrapper(version))
		return models