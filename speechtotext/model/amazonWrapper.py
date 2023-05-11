"""Modelwrapper implemented for Amazon STT API.

AMAZON API. AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AMAZON_REGION and AMAZON_BUCKET  need to be in the '.env'.

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.model.amazonWrapper import *
	from speechtotext.benchmark.benchmarks import *
	from speechtotext.datasets import Dataset
	
	# Create dataset
	number_of_samples = 10
	dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
	id = "existing_audio_id"
	number_of_samples = 10
	
	# Create wrapper
	amazonWrapper = AmazonAPIVersion(AmazonAPIVersion.AMAZON_DEFAULT)

	# Get model
	amazonWrapper.get_model()

	# Benchmark choisen sample
	amazonWrapper.benchmark_sample(dataset, id)
	
	# Benchmark n random samples
	array = amazonWrapper.benchmark_n_samples(dataset, number_of_samples)
"""

import urllib.request
import json
import time
import boto3

from speechtotext.model.modelWrapper import *
from speechtotext.functions import get_extention_of_file_name, string_cleaning, load_env_variable, NoTranscriptReturned

class AmazonNoTranscriptReturned(NoTranscriptReturned):
	"""Exception when Amazon API does not return a transcript.
	"""    
	def __init__(self):     
				
		super().__init__("Results not found")


class AmazonAPIVersion(ModelVersion):
	"""Enum for the available AMAZON API models. This is for the  `Custom language model <https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateLanguageModel.html>`_.

	Args:
		Enum (AmazonAPIVersion): Available whisper API models.
	"""
	AMAZON_DEFAULT 	= "AmazonApi"
	"""Default model version.
	"""


class AmazonAPIWrapper(ModelWrapper): 
	"""Wrapper for AMAZON API. AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AMAZON_REGION and AMAZON_BUCKET need to be in the '.env' file in current directory.
 	"""

	LANGUAGE_CODE:str = 'nl-NL'
	"""str: Code for the language to transcribe.
	
	See  `supported languages for amazon <https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html>`_
	"""
	BUCKET_EXIST:bool = True
	"""bool: Boolean that represents if the bucket exists.
	"""	
	

	def __init__(self, model_version:AmazonAPIVersion):
		"""Wrapper for AMAZON model.

		Args:
			model_version (AmazonAPIVersion): Model version of AMAZON STT API to use.
		"""     
		super().__init__(model_version)

	def get_model(self):
		"""Get model.
		"""		  
		
		load_env_variable("AWS_ACCESS_KEY_ID"), load_env_variable("AWS_SECRET_ACCESS_KEY")
		self.BUCKET = load_env_variable("AMAZON_BUCKET")
		self.AMAZON_REGION = load_env_variable("AMAZON_REGION")

		self.s3 = boto3.resource('s3')
		self.client = boto3.client('s3')
		if AmazonAPIWrapper.BUCKET_EXIST is False:
			self.client.create_bucket(
				ACL = 'private',
				Bucket=self.BUCKET
			)
			AmazonAPIWrapper.BUCKET_EXIST = True
			print(f"bucket created with name {self.BUCKET}")

	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file with API call.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""

		# Upload
		# object_name = get_file_name_without_extention(audio_file_name)
		self.s3.Bucket(self.BUCKET).upload_file(audio_file_name, audio_file_name)

		# Transcribe
		transcribe_client = boto3.client('transcribe', region_name = self.AMAZON_REGION)
		file_uri = f's3://{self.BUCKET}/{audio_file_name}'
		transcriptFileUri = self._get_transcribe_file_location(file_uri, transcribe_client, f"Transcribe-{string_cleaning(audio_file_name)}")

		return self._get_transcript_from_json_uri(transcriptFileUri)

	def _get_transcript_from_json_uri(self, json_uri:str)-> str:
		"""Get transcript from amazon transcribe json result.

		Args:
			json_uri (str): Uri of the resulting json file.

		Returns:
			str: Transcript of the audio.
		"""     
		with urllib.request.urlopen(json_uri) as response:
			data = json.load(response)
			return data.get("results").get("transcripts")[0].get("transcript")

	def _get_transcribe_file_location(self, file_uri:str, transcribe_client, job_name:str="Transcribe") ->str:
		"""Transcribe and return result location. 

		Args:
			file_uri (str): S3 path to audio file.
			transcribe_client (_type_): Boto3 transcribe client.
			file_ext (str): File extention of audio file.
			job_name (str, optional): Name of amazon AWS job. Defaults to "Transcribe".
		"""	
		try:
			transcribe_client.start_transcription_job(
				TranscriptionJobName = job_name,
				Media = {
					'MediaFileUri': file_uri
				},
				MediaFormat = get_extention_of_file_name(file_uri)[1:], #removed the .
				LanguageCode = self.LANGUAGE_CODE
			)
		except:
			pass

		max_tries = 60
		while max_tries > 0:
			max_tries -= 1
			job = transcribe_client.get_transcription_job(TranscriptionJobName = job_name)
			job_status = job['TranscriptionJob']['TranscriptionJobStatus']
			if job_status in ['COMPLETED', 'FAILED']:
				# print(f"Job {job_name} is {job_status}.")
				if job_status == 'COMPLETED':
					download_uri:str = job['TranscriptionJob']['Transcript']['TranscriptFileUri']
				if job_status == 'FAILED':
					raise AmazonNoTranscriptReturned()
				break
			else:
				# print(f"Waiting for {job_name}. Current status is {job_status}.")
				pass
			time.sleep(10)
		response = transcribe_client.delete_transcription_job(
			TranscriptionJobName=job_name
		)
		return download_uri