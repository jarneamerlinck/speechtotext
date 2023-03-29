"""Module with the parent classes for the model wrapper. Needs to be implemented to use the benchmarks.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.models.moduleWrapper import *
	from speechtotext.benchmarks import *
	from speechtotext.datasets import Dataset
 
	# Create child class for ModelVersion
	class ChildModelVersion(ModelVersion):
		MODEL_VERSION 	= "demo"

	# Create child class for ModelWrapper
	class ChildModelWrapper(ModelWrapper): 
		def __init__(self, model_version:ChildModelVersion):
	
			self.model_version = model_version

		def get_model(self, model:modelType):
			self.model = model

		def get_transcript_of_file(self, audio_file_name:str) -> str:  
			result = self.model.transcribe(audio_file_name)
			return result["text"]
   
	# Create child class of benchmark 
	class ChildBenchmark(Benchmark):  
		MODEL_BASE = "model_name"
		
		def create_models(self) -> list[ModelWrapper]:
			models = []
			for version in ChildModelVersion:
				models.append(ChildModelWrapper(version))
			return models
   
	# Create benchmark
	number_of_samples = 10
	dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
	Benchmark.set_dataset(dataset)

	benchmark = ChildBenchmark()
 
	# Run benchmark
	benchmark(number_of_samples)
"""
from enum import Enum
from abc import ABC, abstractmethod
from speechtotext.datasets import Dataset, SampleDataset
from speechtotext.metrics import Metrics
import pandas as pd


class ModelVersion(Enum):
	"""Enum for the availible models.

	Args:
		Enum (ModelVersion): Availible models.
	"""
	pass

class ModelWrapper(ABC):
	"""Abstract Wrapper for model.
	"""    


	def __init__(self, model_version:ModelVersion):
		"""Wrapper for models.

		Args:
			model_version (WhisperModel): Model version of whisper to use.
		"""     
		self.model_version = model_version
	
	@abstractmethod
	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""		
		pass


	@abstractmethod
	def get_model(self):
		"""Get model. Set self.model.
		"""     
		pass

	def benchmark_sample(self, dataset:Dataset, id:str, with_cleaning=True)-> Metrics:
		"""Benchmark sample with model.

		Args:
			dataset (Dataset): Dataset of audio.
			id (str): Id of audio file.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.

		Returns:
			Metrics: Metrics of the transcript.
		"""     
		self.get_model()
		reference = dataset.get_text_of_id(id)
		hypothesis = self.get_transcript_of_file(dataset.get_path_of_fragment(id))
		m = Metrics(reference,hypothesis, id, with_cleaning)
		return m

	def benchmark_n_samples(self, dataset:Dataset, number_of_samples:int, with_cleaning=True) -> list:
		"""Benchmark n samples with model.

		Args:
			dataset (Dataset): Dataset of audio.
			number_of_samples (int): Number of random samples to benchmerk.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.

		Returns:
			list: list of metrics for each sample.
		"""     
		samples = dataset.get_n_samples(number_of_samples)
		return self.benchmark_samples(samples, with_cleaning)


	def benchmark_samples(self, samples: SampleDataset, with_cleaning=True) -> list:
		"""Benchmark samples with model.

		Args:
			dataset (Dataset): Dataset of audio.
			number_of_samples (int): Number of random samples to benchmerk.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.

		Returns:
			list: list of metrics for each sample.
		"""     
		metrics_array = []
  
		for _, row in samples.dataset.iterrows():
			id = row["id"]
			metrics_array.append(self.benchmark_sample(samples, id, with_cleaning))

		return metrics_array
		