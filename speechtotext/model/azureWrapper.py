"""Modelwrapper implemented for Azure STT API.

AZURE_SPEECH_KEY API and AZURE_SPEECH_REGION need to be in the '.env'.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.model.azureWrapper import *
	from speechtotext.benchmark.benchmarks import *
	from speechtotext.datasets import Dataset
	
	# Create dataset
	number_of_samples = 10
	dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
	id = "existing_audio_id"
	number_of_samples = 10
	
	# Create wrapper
	azureWrapper = AzureAPIVersion(AzureAPIVersion.AZURE_DEFAULT)

	# Get model
	azureWrapper.get_model()

	# Benchmark choisen sample
	azureWrapper.benchmark_sample(dataset, id)
	
	# Benchmark n random samples
	array = azureWrapper.benchmark_n_samples(dataset, number_of_samples)
"""
import azure.cognitiveservices.speech as speechsdk

from speechtotext.model.modelWrapper import *
from speechtotext.functions import get_extention_of_file_name, string_cleaning, load_env_variable

class AzureNoMatch(Exception):
	"""Exception when Azure finds not match.
	"""
	def __init__(self, message:str):
		"""_summary_

		Args:
			message (str): Error message.
		"""
		super().__init__(f"No speech could be recognized: {message}")

class AzureCancellation(Exception):
	"""Exception when Azure gives an cancelation message.
	"""
	def __init__(self, message:str):
		"""_summary_

		Args:
			message (str): Error message.
		"""     
		super().__init__(f"Canceled: {message}")

class AzureAPIVersion(ModelVersion):
	"""Enum for the available AZURE API models. 
	Args:
		Enum (AzureAPIVersion): Available whisper API models.
	"""
	AZURE_DEFAULT 	= "AzureApi"
	"""Default model version.
	"""

class AzureAPIWrapper(ModelWrapper):
	"""Wrapper for AZURE API. AZURE_SPEECH_KEY API and AZURE_SPEECH_REGION need to be in the '.env' file in current directory.
	"""
	LANGUAGE_CODE:str = 'nl-BE'
	"""str: Code for the language to transcribe.
	
	See `supported languages for azure <https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt>`_
	"""

	def __init__(self, model_version:AzureAPIVersion):
		"""Wrapper for AZURE model.

		Args:
			model_version (AzureAPIVersion): Model version of AZURE STT API to use.
		"""
		super().__init__(model_version)

	def get_model(self):
		"""Get model.
		"""
		self.AZURE_SPEECH_KEY = load_env_variable("AZURE_SPEECH_KEY")
		self.AZURE_SPEECH_REGION = load_env_variable("AZURE_SPEECH_REGION")

		self.speech_config = speechsdk.SpeechConfig(subscription=self.AZURE_SPEECH_KEY, region=self.AZURE_SPEECH_REGION)
		self.speech_config.speech_recognition_language=self.LANGUAGE_CODE

	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file with API call.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""
		audio_config = speechsdk.audio.AudioConfig(filename=audio_file_name)
		speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=audio_config)
		result = speech_recognizer.recognize_once()
		if result.reason == speechsdk.ResultReason.NoMatch:
			raise AzureNoMatch(result.no_match_details)
		if result.reason == speechsdk.ResultReason.Canceled:
			cancellation_details = result.cancellation_details
			# print("Speech Recognition canceled: {}".format(cancellation_details.reason))
			error_message:str = cancellation_details.reason
			if cancellation_details.reason == speechsdk.CancellationReason.Error:
				error_message = f"{error_message}: {cancellation_details.error_details}"
			raise AzureCancellation(error_message)
		return result.text
