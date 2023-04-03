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

from abc import ABC, abstractmethod
import pandas as pd

from speechtotext.benchmark.benchmarks import *
from speechtotext.model.modelWrapper import ModelWrapper
from speechtotext.model.whisperWrapper import WhisperVersion, WhisperWrapper, WhisperAPIWrapper, WhisperAPIVersion
from speechtotext.model.amazonWrapper import AmazonAPIVersion, AmazonAPIWrapper
from speechtotext.model.googleWrapper import GoogleAPIVersion, GoogleAPIWrapper


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

class AmazonAPIBenchmark(Benchmark):
	"""Benchmark for Amazon API transcribe.
	"""
	MODEL_BASE = "AmazonAPI"

	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in AmazonAPIVersion:
			models.append(AmazonAPIWrapper(version))
		return models

class GoogleAPIBenchmark(Benchmark):
	"""Benchmark for Google API transcribe.
	"""
	MODEL_BASE = "GoogleAPI"

	def create_models(self) -> list[ModelWrapper]:
		models = []
		for version in GoogleAPIVersion:
			models.append(GoogleAPIWrapper(version))
		return models

