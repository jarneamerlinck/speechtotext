"""Modelwrapper implemented for deepgram API.

DEEPGRAM_API_KEY needs to be in the '.env'.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.model.deepgramWrapper import *
	from speechtotext.benchmark.benchmarks import *
	from speechtotext.datasets import Dataset
	
	# Create dataset
	number_of_samples = 10
	dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
	id = "existing_audio_id"
	number_of_samples = 10
	
	# Create wrapper
	deepgramWrapper = deepgramAPIVersion(deepgramAPIVersion.deepgram_DEFAULT)

	# Get model
	deepgramWrapper.get_model()

	# Benchmark choisen sample
	deepgramWrapper.benchmark_sample(dataset, id)
	
	# Benchmark n random samples
	array = deepgramWrapper.benchmark_n_samples(dataset, number_of_samples)
"""

from deepgram import Deepgram
import json
import io

from speechtotext.model.modelWrapper import *
from speechtotext.functions import load_env_variable

class DeepgramAPIVersion(ModelVersion):
	"""Enum for the available deepgram API models.

	Args:
		Enum (deepgramAPIVersion): Available whisper API models.
	"""
	DEEPGRAM_DEFAULT 	= "general"
	DEEPGRAM_ENHANCED	= "general-enhanced"



class DeepgramAPIWrapper(ModelWrapper): 
	"""Wrapper for deepgram API. DEEPGRAM_API_KEY needs to be in the '.env' file in current directory.
 	"""

	LANGUAGE_CODE:str = 'nl'

	def __init__(self, model_version:DeepgramAPIVersion):
		"""Wrapper for deepgram model.

		Args:
			model_version (deepgramAPIVersion): Model version of deepgram STT API to use.
		"""     
		self.model_version = model_version

	def get_model(self):
		"""Get model.
		"""		  
		
		DEEPGRAM_API_KEY = load_env_variable("DEEPGRAM_API_KEY")
		self.client  = Deepgram(DEEPGRAM_API_KEY)

	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file with API call.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""
		with open(audio_file_name, 'rb') as audio:
			source = {'buffer': audio, 'mimetype': 'audio/wav'}
			response = self.client.transcription.sync_prerecorded(source, 
														 {'punctuate': False, 
														  'language':self.LANGUAGE_CODE, 
														  'model': self.model_version.value})
			
			transcript = response.get("results").get("channels")[0].get("alternatives")[0].get("transcript")
			return transcript
