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
"""

from abc import ABC
import pandas as pd

from speechtotext.benchmark.benchmarks import *
from speechtotext.model.modelWrapper import ModelWrapper
from speechtotext.model.whisperWrapper import WhisperVersion, WhisperWrapper, WhisperAPIWrapper, WhisperAPIVersion
from speechtotext.model.amazonWrapper import AmazonAPIVersion, AmazonAPIWrapper
from speechtotext.model.googleWrapper import GoogleAPIVersion, GoogleAPIWrapper
from speechtotext.model.deepgramWrapper import DeepgramAPIVersion, DeepgramAPIWrapper
from speechtotext.model.assemblyAIWrapper import AssemblyAIAPIVersion, AssemblyAIAPIWrapper
from speechtotext.model.azureWrapper import AzureAPIVersion, AzureAPIWrapper
from speechtotext.model.speechmaticsWrapper import SpeechmaticsAPIVersion, SpeechmaticsAPIWrapper


class WhisperBenchmark(Benchmark):
	"""Benchmark for local whisper models.
	"""
	MODEL_BASE:str = "Whisper"
	"""str: Name of base model.
	"""
	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in WhisperVersion:
			models.append(WhisperWrapper(version))
		return models

class WhisperAPIBenchmark(Benchmark):
	"""Benchmark for API whisper models.
	"""
	MODEL_BASE:str = "WhisperAPI"
	"""str: Name of base model.
	"""
	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in WhisperAPIVersion:
			models.append(WhisperAPIWrapper(version))
		return models

class AmazonAPIBenchmark(Benchmark):
	"""Benchmark for Amazon API transcribe.
	"""
	MODEL_BASE:str = "AmazonAPI"
	"""str: Name of base model.
	"""
	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in AmazonAPIVersion:
			models.append(AmazonAPIWrapper(version))
		return models

class GoogleAPIBenchmark(Benchmark):
	"""Benchmark for Google API transcribe.
	"""
	MODEL_BASE:str = "GoogleAPI"
	"""str: Name of base model.
	"""
	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in GoogleAPIVersion:
			models.append(GoogleAPIWrapper(version))
		return models

class DeepgramAPIBenchmark(Benchmark):
	"""Benchmark for Deepgram API.
	"""
	MODEL_BASE:str = "DeepgramAPI"
	"""str: Name of base model.
	"""
	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in DeepgramAPIVersion:
			models.append(DeepgramAPIWrapper(version))
		return models

class AssemblyAIAPIBenchmark(Benchmark):
	"""Benchmark for AssemblyAI API.
	"""
	MODEL_BASE:str = "AssemblyAIAPI"
	"""str: Name of base model.
	"""
	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in AssemblyAIAPIVersion:
			models.append(AssemblyAIAPIWrapper(version))
		return models

class AzureAPIBenchmark(Benchmark):
	"""Benchmark for Azure API.
	"""
	MODEL_BASE:str = "AzureAPI"
	"""str: Name of base model.
	"""
	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in AzureAPIVersion:
			models.append(AzureAPIWrapper(version))
		return models

class SpeechmaticsAPIBenchmark(Benchmark):
	"""Benchmark for Speechmatics API.
	"""
	MODEL_BASE:str = "SpeechmaticsAPI"
	"""str: Name of base model.
	"""
	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in SpeechmaticsAPIVersion:
			models.append(SpeechmaticsAPIWrapper(version))
		return models
