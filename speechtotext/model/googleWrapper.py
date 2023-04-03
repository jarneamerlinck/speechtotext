"""Modelwrapper implemented for google STT API.

GOOGLE_APPLICATION_CREDENTIALS needs to be in the '.env'.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.model.googleWrapper import *
	from speechtotext.benchmark.benchmarks import *
	from speechtotext.datasets import Dataset
	
	# Create dataset
	number_of_samples = 10
	dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
	id = "existing_audio_id"
	number_of_samples = 10
	
	# Create wrapper
	googleWrapper = googleAPIVersion(googleAPIVersion.google_DEFAULT)

	# Get model
	googleWrapper.get_model()

	# Benchmark choisen sample
	googleWrapper.benchmark_sample(dataset, id)
	
	# Benchmark n random samples
	array = googleWrapper.benchmark_n_samples(dataset, number_of_samples)
"""

from google.cloud import speech_v2
from google.cloud import speech
from google.oauth2 import service_account
import json
import io

from speechtotext.model.modelWrapper import *
from speechtotext.functions import load_env_variable

class GoogleAPIVersion(ModelVersion):
	"""Enum for the available google API models.

	Args:
		Enum (googleAPIVersion): Available whisper API models.
	"""
	GOOGLE_DEFAULT 	= "googleApi"
	# GOOGLE_V2 	= "googleApi"



class GoogleAPIWrapper(ModelWrapper): 
	"""Wrapper for google API. GOOGLE_APPLICATION_CREDENTIALS needs to be in the '.env' file in current directory.
 	"""

	LANGUAGE_CODE:str = 'nl-BE'

	def __init__(self, model_version:GoogleAPIVersion):
		"""Wrapper for google model.

		Args:
			model_version (googleAPIVersion): Model version of google STT API to use.
		"""     
		self.model_version = model_version

	def get_model(self):
		"""Get model.
		"""		  
		
		credentials_json = load_env_variable("GOOGLE_APPLICATION_CREDENTIALS")
		with open(credentials_json, 'r') as file:
			self.credentials_data = json.load(file)
		credentials = service_account.Credentials.from_service_account_file(credentials_json)
		self.client = speech.SpeechClient(credentials=credentials)


	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file with API call.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""
		with io.open(audio_file_name, "rb") as audio_file:
			content = audio_file.read()

		audio = speech.RecognitionAudio(content=content)
		config = speech.RecognitionConfig(
			encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
			# sample_rate_hertz=8000,
			language_code=self.LANGUAGE_CODE,
			# use_enhanced=True,
			# # A model must be specified to use enhanced model.
			# model="phone_call",
		)

		response = self.client.recognize(config=config, audio=audio)

		for i, result in enumerate(response.results):
			
			alternative = result.alternatives[0].transcript
			break
		return str(alternative)
