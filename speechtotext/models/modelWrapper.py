from enum import Enum
import whisper
import os
from abc import ABC, abstractmethod
from speechtotext.datasets import Dataset
from speechtotext.metrics import Metrics



class ModelVersion(Enum):
	"""Enum for the availible models

	Args:
		Enum (ModelVersion): Availible models
	"""
	pass



class ModelWrapper(ABC):
	"""Abstract Wrapper for model
	"""    


	def __init__(self, model_version:ModelVersion):
		"""Wrapper for models

		Args:
			model_version (WhisperModel): Model version of whisper to use
		"""     
		self.model_version = model_version
	
	@abstractmethod
	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file

		Args:
			audio_file_name (str): Path to audio file

		Returns:
			str: Transcript of audio file
		"""		
		pass


	@abstractmethod
	def get_model(self):
		"""Get model. Set self.model
		"""     
		pass

	def benchmark_sample(self, dataset:Dataset, id:str)-> Metrics:
		"""Benchmark sample with model

		Args:
			dataset (Dataset): Dataset of audio
			id (str): Id of audio file

		Returns:
			Metrics: Metrics of the transcript
		"""     
		self.get_model()
		reference = dataset.get_text_of_id(id)
		hypothesis = self.get_transcript_of_file(dataset.get_path_of_fragment(id))
		m = Metrics(reference,hypothesis)
		return m

	def benchmark_n_samples(self, dataset:Dataset, number_of_samples:int) -> list:
		"""Benchmark n samples with model

		Args:
			dataset (Dataset): Dataset of audio
			number_of_samples (int): Number of random samples to benchmerk

		Returns:
			list: list of metrics for each sample
		"""     
		metrics_array = []

		if number_of_samples > dataset.number_of_samples():
			print("number larger then samples in dataset. Using full dataset")
			number_of_samples = dataset.number_of_samples()

		df = dataset.dataset.sample(n=number_of_samples)
		for index, row in df.iterrows():
			id = row["id"]
			metrics_array.append(self.benchmark_sample(dataset, id))

		return metrics_array
		