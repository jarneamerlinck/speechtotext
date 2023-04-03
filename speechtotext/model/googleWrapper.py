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
from google.oauth2 import service_account


from speechtotext.model.modelWrapper import *
from speechtotext.functions import load_env_variable

class GoogleAPIVersion(ModelVersion):
	"""Enum for the available google API models.

	Args:
		Enum (googleAPIVersion): Available whisper API models.
	"""
	GOOGLE_DEFAULT 	= "googleApi"



class GoogleAPIWrapper(ModelWrapper): 
	"""Wrapper for google API. GOOGLE_APPLICATION_CREDENTIALS needs to be in the '.env' file in current directory.
 	"""


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
		credentials = service_account.Credentials.from_service_account_file(credentials_json)
		self.client = speech_v2.SpeechClient(credentials=credentials)


	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file with API call.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""
		audio_file = open(audio_file_name, "rb")
		project, location, recognizer = "", "", ""
		request = speech_v2.RecognizeRequest(
			content=audio_file,
			recognizer=f"projects/{project}/locations/{location}/recognizers/{recognizer}",
			)
		audio_file.close()
		response = self.client.recognize(request=request)


		transcript = str(response)
		return transcript
