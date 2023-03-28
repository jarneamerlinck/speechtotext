from speechtotext.models.modelWrapper import *
import whisper

class WhisperVersion(ModelVersion):
	"""Enum for the available Whisper models

	Args:
		Enum (WhisperModel): Available whisper models
	"""
	TINY 	= "tiny"
	SMALL 	= "small"
	MEDIUM 	= "medium"
	LARGE 	= "large"
	BASE 	= "base"

class WhisperWrapper(ModelWrapper): 
	"""Wrapper for whisper model

	"""    
	MODEL_DIR = "models/whisper"

	def __init__(self, model_version:WhisperVersion):
		"""Wrapper for whisper model

		Args:
			model_version (WhisperVersion): Model version of whisper to use
		"""     
		self.model_version = model_version

	def get_model(self):
		"""Get model
		"""     
		self.model = whisper.load_model(self.model_version.value)

	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file

		Args:
			audio_file_name (str): Path to audio file

		Returns:
			str: Transcript of audio file
		"""		
		result = self.model.transcribe(audio_file_name)
		return result["text"]
		