"""Modelwrapper implemented for Speechmatics STT API.

.. warning::

	Package version speechmatics-python==1.6.4 is needed to run the script. Errors on 1.7.0

SPEECHMATICS_API_KEY needs to be in the '.env' file in current directory.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.model.speechmaticsWrapper import *
	from speechtotext.benchmark.benchmarks import *
	from speechtotext.datasets import Dataset
	
	# Create dataset
	number_of_samples = 10
	dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
	id = "existing_audio_id"
	number_of_samples = 10
	
	# Create wrapper
	speechmaticsWrapper = SpeechmaticsAPIVersion(SpeechmaticsAPIVersion.SPEECHMATICS_DEFAULT)

	# Get model
	speechmaticsWrapper.get_model()

	# Benchmark choisen sample
	speechmaticsWrapper.benchmark_sample(dataset, id)
	
	# Benchmark n random samples
	array = speechmaticsWrapper.benchmark_n_samples(dataset, number_of_samples)
"""
import speechmatics
import nest_asyncio

from speechtotext.model.modelWrapper import *
from speechtotext.functions import get_extention_of_file_name, string_cleaning, load_env_variable


class SpeechmaticsAPIVersion(ModelVersion):
	"""Enum for the available SPEECHMATICS API models. 
	Args:
		Enum (SpeechmaticsAPIVersion): Available whisper API models.
	"""
	SPEECHMATICS_DEFAULT 	= "SpeechmaticsApi"

class SpeechmaticsAPIWrapper(ModelWrapper): 
	"""Wrapper for SPEECHMATICS API. SPEECHMATICS_API_KEY needs to be in the '.env' file in current directory.
 	"""
	LANGUAGE_CODE:str = 'nl'
	CONNECTION_URL = f"wss://eu2.rt.speechmatics.com/v2/"	
 
	def __init__(self, model_version:SpeechmaticsAPIVersion):
		"""Wrapper for SPEECHMATICS model.

		Args:
			model_version (SpeechmaticsAPIVersion): Model version of SPEECHMATICS STT API to use.
		"""     
		self.partial_transcripts:list[str] = []
		nest_asyncio.apply()
		super().__init__(model_version)
  
	def __api_event_handler(self, msg:dict):
		"""Event handler for API.

		Args:
			msg (dict): api result.
		"""     
		self.partial_transcripts.append(msg.get("metadata").get("transcript"))

	def get_model(self):
		"""Get model.
		"""
		self.SPEECHMATICS_API_KEY = load_env_variable("SPEECHMATICS_API_KEY")
 
		self.ws = speechmatics.client.WebsocketClient(

			speechmatics.models.ConnectionSettings(
				url=self.CONNECTION_URL+self.LANGUAGE_CODE,
				auth_token=self.SPEECHMATICS_API_KEY,
				generate_temp_token=True,
			)
		)
		self.ws.add_event_handler(
			event_name=speechmatics.models.ServerMessageType.AddTranscript,
			event_handler=self.__api_event_handler,
		)
		self.settings = speechmatics.models.AudioSettings()
		self.conf = speechmatics.models.TranscriptionConfig(
			language=self.LANGUAGE_CODE,
			enable_partials=False,
			max_delay=5,
			enable_entities=False,
		)

	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file with API call.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""
		with open(audio_file_name, "rb") as f:
			try:
				self.ws.run_synchronously(f, self.conf, self.settings)
			except Exception as e:
				pass
		
		result =  ''.join(self.partial_transcripts)
		self.partial_transcripts = []
		result = string_cleaning(result)[:-1] # remove space at end of transcript

		return result