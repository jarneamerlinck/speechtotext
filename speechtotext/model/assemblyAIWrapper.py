"""Modelwrapper implemented for assemblyAi API.

ASSEMBLY_AI_API_KEY needs to be in the '.env'.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.model.assemblyAiWrapper import *
	from speechtotext.benchmark.benchmarks import *
	from speechtotext.datasets import Dataset
	
	# Create dataset
	number_of_samples = 10
	dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
	id = "existing_audio_id"
	number_of_samples = 10
	
	# Create wrapper
	assemblyAiWrapper = assemblyAiAPIVersion(assemblyAiAPIVersion.assemblyAi_DEFAULT)

	# Get model
	assemblyAiWrapper.get_model()

	# Benchmark choisen sample
	assemblyAiWrapper.benchmark_sample(dataset, id)
	
	# Benchmark n random samples
	array = assemblyAiWrapper.benchmark_n_samples(dataset, number_of_samples)
"""

import requests
import time

from speechtotext.model.modelWrapper import *
from speechtotext.functions import load_env_variable, string_cleaning

class AssemblyAIAPIVersion(ModelVersion):
	"""Enum for the available assemblyAi API models.

	Args:
		Enum (assemblyAiAPIVersion): Available whisper API models.
	"""
	ASSEMBLYAI_DEFAULT 	= "default"
	"""Default model version.
	"""



class AssemblyAIAPIWrapper(ModelWrapper): 
	"""Wrapper for assemblyAi API. ASSEMBLY_AI_API_KEY needs to be in the '.env' file in current directory.
 	"""

	LANGUAGE_CODE:str = 'nl'
	"""str: Code for the language to transcribe.
	
	See  `supported languages for assemblyAi <https://www.assemblyai.com/docs/#supported-languages>`_
	"""
	API_URL:str = "https://api.assemblyai.com/v2/upload"
	"""str: Connection url for the API.
	"""
	UPLOAD_ENDPOINT:str = "https://api.assemblyai.com/v2/upload"
	"""str: Upload endpoint url.
	"""
	TRANSCRIPT_ENDPOINT:str = "https://api.assemblyai.com/v2/transcript"
	"""str: Transcribe endpoint url.
	"""
	POLLING_ENDPOINT:str = "https://api.assemblyai.com/v2/transcript/"
	"""str: Polling endpoint url.
	"""
	TIME_SLEEP:int = 3
	"""int: Time to sleep after each polling.
	"""

	def __init__(self, model_version:AssemblyAIAPIVersion):
		"""Wrapper for assemblyAi model.

		Args:
			model_version (assemblyAiAPIVersion): Model version of assemblyAi STT API to use.
		"""     
		super().__init__(model_version)

	def get_model(self):
		"""Get model.
		"""
		self.ASSEMBLY_AI_API_KEY = load_env_variable("ASSEMBLY_AI_API_KEY")

	def _read_file_with_chunck_size(self, audio_file_name:str, chunk_size:int=5242880):
		"""Read data from file.

		Args:
			audio_file_name (str): Path to audio file.
			chunk_size (int, optional): Size of chunk. Defaults to 5242880.

		Yields:
			generator: Audio file.
		"""     
		with open(audio_file_name, "rb") as _file:
			while True:
				data = _file.read(chunk_size)
				if not data:
					break
				yield data
	
	def _upload_file(self, audio_file_name:str, header:dict) -> dict:
		"""Upload file.

		Args:
			audio_file_name (str): Path to audio file.
			header (dict): Http header.

		Returns:
			dict: Url for request.
		"""     
		upload_response = requests.post(
			self.UPLOAD_ENDPOINT,
			headers=header, data=self._read_file_with_chunck_size(audio_file_name)
		)
		return upload_response.json()

	def _request_transcript(self, upload_url:dict, header:dict) -> dict:
		"""Request transcript.

		Args:
			upload_url (dict): Url for request.
			header (dict): Http header.

		Returns:
			dict: Response of request.
		"""     
		transcript_request = {
			'audio_url': upload_url['upload_url'],
			"language_code": self.LANGUAGE_CODE
		}
		transcript_response = requests.post(
			self.TRANSCRIPT_ENDPOINT,
			json=transcript_request,
			headers=header
		)
		return transcript_response.json()

	def _make_polling_endpoint(self, transcript_response:dict) -> str:
		"""Make polling endoint.

		Args:
			transcript_response (dict): Transcript response.

		Returns:
			str: Polling endpoint.
		"""     
		polling_endpoint = self.POLLING_ENDPOINT
		polling_endpoint += transcript_response['id']
		return polling_endpoint

	def _wait_for_completion(self, polling_endpoint:str, header:dict):
		"""Wait for the translation to be done.

		Args:
			polling_endpoint (str): Polling endpoint.
			header (dict): Http header.
		"""     
		while True:
			polling_response = requests.get(polling_endpoint, headers=header)
			polling_response = polling_response.json()

			if polling_response['status'] == 'completed':
				break

			time.sleep(self.TIME_SLEEP)

	def _get_paragraphs(self, polling_endpoint:str, header:dict) -> list:
		"""Get results from polling endpoint.

		Args:
			polling_endpoint (str): Polling endpoint.
			header (dict): Http header.

		Returns:
			list: Transcript of audio file in list.
		"""     
		paragraphs_response = requests.get(polling_endpoint + "/paragraphs", headers=header)
		paragraphs_response = paragraphs_response.json()

		paragraphs = []
		for para in paragraphs_response['paragraphs']:
			paragraphs.append(para)

		return paragraphs

	def _clean_output(self, paragraphs:list)-> str:
		"""Transcript list to 1 string.

		Args:
			paragraphs (list): Transcript list.

		Returns:
			str: Transcript.
		"""     
		full_result = ""
		for para in paragraphs:
			full_result = full_result+ para['text'] + '\n'
		if full_result[-1]=='\n':
			full_result = full_result[:-1]
		full_result = string_cleaning(full_result)
		return full_result

	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file with API call.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""
		header = {
		'authorization': self.ASSEMBLY_AI_API_KEY,
		'content-type': 'application/json'
		
		}
		upload_url = self._upload_file(audio_file_name, header)
		transcript_response = self._request_transcript(upload_url, header)

		polling_endpoint = self._make_polling_endpoint(transcript_response)

		# Wait until the transcription is complete
		self._wait_for_completion(polling_endpoint, header)

		paragraphs = self._get_paragraphs(polling_endpoint, header)
		return self._clean_output(paragraphs)