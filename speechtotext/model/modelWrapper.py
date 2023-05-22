"""Module with the parent classes for the model wrapper. Needs to be implemented to use the benchmarks.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.model.moduleWrapper import *
	from speechtotext.benchmark.benchmarks import *
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
import os
from urllib.error import HTTPError
from pydub import AudioSegment
import pandas as pd
from  torch.cuda import OutOfMemoryError
from speechtotext.datasets import Dataset, SampleDataset
from speechtotext.metric.metrics import Metrics
from speechtotext.functions import timing, NoTranscriptReturned

class MetaModelWrapper(type):
	"""Meta class for model wrapper.

	Created to automaticly convert a sample before transcribing.
	"""	

	@staticmethod
	def wrap(get_transcript_of_file):
		"""Return a wrapped instance method"""
		def outer(self, path_to_sample):
			self.convert_sample(path_to_sample)
			return_value = get_transcript_of_file(self, self.PATH_OF_TEMP_CONVERTED_AUDIO_FILE)
			os.remove(self.PATH_OF_TEMP_CONVERTED_AUDIO_FILE)
			if not str(return_value):
				raise NoTranscriptReturned()
			return return_value
		return outer

	def __new__(cls, name, bases, attrs):
		"""If the class has a 'get_transcript_of_file' method, wrap it"""
		if 'get_transcript_of_file' in attrs:
			attrs['get_transcript_of_file'] = cls.wrap(attrs['get_transcript_of_file'])
		return super(MetaModelWrapper, cls).__new__(cls, name, bases, attrs)

class ModelVersion(Enum):
	"""Enum for the Available models.

	Args:
		Enum (ModelVersion): Available models.
	"""
	pass

class ModelWrapper(metaclass=MetaModelWrapper):
	"""Abstract Wrapper for model.

	If audio needs to be converted use convert_sample in get_transcript_of_file.
	"""    

	PATH_OF_TEMP_CONVERTED_AUDIO_FILE:str = "converted_audio_file.wav"
	"""PATH_OF_TEMP_CONVERTED_AUDIO_FILE: path to temp file that will be created to convert the audio files to an accepted audio format.
	"""

	def __init__(self, model_version:ModelVersion):
		"""Wrapper for models.

		Args:
			model_version (WhisperModel): Model version of whisper to use.
		"""     
		self.model_version = model_version
		self.column_names_errors = ["audio_ID","dataset", "reference", "message"]
		self.model_errors = pd.DataFrame(columns=self.column_names_errors)	
	
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

	@timing
	def _benchmark_sample_with_time(self, dataset:Dataset, audio_id:str, with_cleaning=True)-> tuple[str, str, float]:
		"""Benchmark sample for model with timer.

		Args:
			dataset (Dataset): Dataset of audio.
			id (str): Id of audio file.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.

		Returns:
			Metrics: Metrics of the transcript.
		"""     
		self.get_model()
		reference = dataset.get_text_of_id(audio_id)
		path_to_sample = dataset.get_path_of_fragment(audio_id)
		hypothesis = self.get_transcript_of_file(path_to_sample)
		return reference, hypothesis


	def benchmark_sample(self, dataset:Dataset, audio_id:str, with_cleaning=True)-> Metrics:
		"""Benchmark sample with model.

		Args:
			dataset (Dataset): Dataset of audio.
			id (str): Id of audio file.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.

		Returns:
			Metrics: Metrics of the transcript.
		"""
		(reference, hypothesis), duration = self._benchmark_sample_with_time(dataset, audio_id, with_cleaning)
		m = Metrics(reference,hypothesis, audio_id, duration, with_cleaning)
		return m

	def benchmark_n_samples(self, dataset:Dataset, number_of_samples:int, with_cleaning=True) -> list:
		"""Benchmark n samples with model.

		Args:
			dataset (Dataset): Dataset of audio.
			number_of_samples (int): Number of random samples to benchmerk.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.

		Returns:
			list: List of metrics for each sample.
		"""     
		samples = dataset.get_n_samples(number_of_samples)
		return self.benchmark_samples(samples, with_cleaning)

	def _append_error(self, samples:SampleDataset, audio_id:str, error:str):
		"""Append error to model_errors.

		Args:
			samples (SampleDataset): Dataset of audio.
			id (str): Id of failed sample.
			error (str): Error message.
		"""     
		new_row = pd.Series([audio_id, samples.name, samples.get_text_of_id(audio_id), error], index=self.column_names_errors)
		self.model_errors = pd.concat([self.model_errors, new_row.to_frame().T], ignore_index=True)

	def convert_sample(self, path_to_sample:str) -> str:
		"""Convert sample to correct format.

		Args:
			path_to_sample (str): Path to sample.
			override (bool, optional): Override original file. Defaults to False.

		Returns:
			str: Path to converted sample.
		"""
		name, ext = os.path.splitext(path_to_sample)
		sound = AudioSegment.from_file(path_to_sample, ext[1:])
		sound = sound.set_channels(1)
  
		sound.export(self.PATH_OF_TEMP_CONVERTED_AUDIO_FILE, format="wav", codec="pcm_s16le")
		return path_to_sample


	def benchmark_samples(self, samples:SampleDataset, with_cleaning=True) -> list:
		"""Benchmark samples with model.

		Args:
			dataset (Dataset): Dataset of audio.
			number_of_samples (int): Number of random samples to benchmerk.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.

		Returns:
			list: List of metrics for each sample.
		"""   
		metrics_array = []

		for _, row in samples.dataset.iterrows():
			audio_id = row["id"]
			try:
				metrics_array.append(self.benchmark_sample(samples, audio_id, with_cleaning))
			except OutOfMemoryError as e:
				error = "CUDA out of memory"
				self._append_error(samples, audio_id, error)

			except HTTPError as e:
				error = f'"{e}"'
				self._append_error(samples, audio_id, error)

			except Exception as e:
				error = f'"{e}"'
				self._append_error(samples, audio_id, error)

		return metrics_array
		