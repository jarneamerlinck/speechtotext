from enum import Enum

import whisper
import os

from speechtotext.datasets import Dataset
from speechtotext.metrics import Metrics



class WhisperModel(Enum):

    TINY 	= "tiny"
    SMALL 	= "small"
    MEDIUM 	= "medium"
    LARGE 	= "large"
    BASE 	= "base"



class Whisper():
	MODEL_DIR = "models/whisper"

	def __init__(self, model_version:WhisperModel):
		self.model_version = model_version

	def get_transcript_of_file(self, audio_file_name:str) -> str:

		result = self.model.transcribe(audio_file_name)
		return result["text"]

	def get_model(self):
		self.model = whisper.load_model(self.model_version.value)
	
	def benchmark_sample(self, dataset:Dataset, id:str)-> Metrics:
		self.get_model()
		reference = dataset.get_text_of_id(id)
		hypothesis = self.get_transcript_of_file(dataset.get_path_of_fragment(id))
		m = Metrics(reference,hypothesis)
		return m