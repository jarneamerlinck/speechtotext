"""Modelwrapper implemented for whisper. Local and API.

For the API OPENAI_API_KEY and OPENAI_ORGANIZATION need to be in the '.env'.
Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.model.whisperWrapper import *
	from speechtotext.benchmark.benchmarks import *
	from speechtotext.datasets import Dataset
	
	# Create dataset
	number_of_samples = 10
	dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
	id = "existing_audio_id"
	number_of_samples = 10
	
	# Create wrapper
	whisperWrapper = WhisperWrapper(WhisperVersion.TINY)

	# Get model
	whisperWrapper.get_model()

	# Benchmark choisen sample
	whisperWrapper.benchmark_sample(dataset, id)
	
	# Benchmark n random samples
	array = whisperWrapper.benchmark_n_samples(dataset, number_of_samples)
"""
import whisper
import openai
import os
from dotenv import load_dotenv

from speechtotext.model.modelWrapper import *

class WhisperVersion(ModelVersion):
	"""Enum for the available Whisper models.

	Args:
		Enum (WhisperVersion): Available whisper models.
	"""
	TINY 	= "tiny"
	SMALL 	= "small"
	MEDIUM 	= "medium"
	LARGE 	= "large"
	BASE 	= "base"

class WhisperWrapper(ModelWrapper): 
	"""Wrapper for whisper model.
	"""

	def __init__(self, model_version:WhisperVersion):
		"""Wrapper for whisper model.

		Args:
			model_version (WhisperVersion): Model version of whisper to use.
		"""     
		self.model_version = model_version

	def get_model(self):
		"""Get model.
		"""     
		self.model = whisper.load_model(self.model_version.value)

	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""		
		result = self.model.transcribe(audio_file_name)
		return result["text"]
		
class WhisperAPIVersion(ModelVersion):
	"""Enum for the available Whisper API models.

	Args:
		Enum (WhisperAPIVersion): Available whisper API models.
	"""
	WHISPER_1 	= "whisper-1"

  
class WhisperAPIWrapper(ModelWrapper): 
	"""Wrapper for whisper API. OPENAI_ORGANIZATION and OPENAI_API_KEY need to be in .env file in current directory.
	"""

	def __init__(self, model_version:WhisperAPIVersion):
		"""Wrapper for whisper model.

		Args:
			model_version (WhisperAPIWrapper): Model version of whisper to use.
		"""     
		self.model_version = model_version

	def get_model(self):
		"""Get model
		"""     
		load_dotenv()
		openai.organization = os.getenv("OPENAI_ORGANIZATION")
		openai.api_key = os.getenv("OPENAI_API_KEY")

	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file with API call.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""		  
		file = open(audio_file_name, "rb")
		transcription = openai.Audio.transcribe(self.model_version.value, file)
		file.close()
		return transcription["text"]