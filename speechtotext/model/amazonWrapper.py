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

import os
import io
import time
import boto3

from speechtotext.model.modelWrapper import *
from speechtotext.functions import get_extention_of_file_name, get_file_name_without_extention, load_env_variable

class AmazonAPIVersion(ModelVersion):
	"""Enum for the available AMAZON API models. This is for the  `Custom language model <https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateLanguageModel.html>`_.

	Args:
		Enum (AmazonAPIVersion): Available whisper API models.
	"""
	AMAZON_DEFAULT 	= "AmazonApi"



class AmazonAPIWrapper(ModelWrapper): 
	"""Wrapper for AMAZON API. AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AMAZON_REGION and AMAZON_BUCKET need to be in the '.env' file in current directory.
 	"""

	LANGUAGE_CODE:str = 'nl-NL'
	BUCKET_EXIST = False

	def __init__(self, model_version:AmazonAPIVersion):
		"""Wrapper for AMAZON model.

		Args:
			model_version (AmazonAPIVersion): Model version of AMAZON STT API to use.
		"""     
		self.model_version = model_version

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

	def get_transcript_of_file(self, audio_file_name:str) -> str:
		"""Get transcript of audio file with API call.

		Args:
			audio_file_name (str): Path to audio file.

		Returns:
			str: Transcript of audio file.
		"""

		# Upload
		object_name = get_file_name_without_extention(audio_file_name)
		self.s3.Bucket(self.BUCKET).upload_file(audio_file_name, object_name)

		# Transcribe
		transcribe_client = boto3.client('transcribe', region_name = self.AMAZON_REGION)
		file_uri = f's3://{self.BUCKET}/{object_name}'
		transcriptFileUri = self.__get_transcribe_file_location(file_uri, transcribe_client)

		# Download transcript
		object = self.s3.Bucket(self.BUCKET).Object(transcriptFileUri)
		file_stream = io.StringIO()
		object.download_fileobj(file_stream)

		return file_stream.getvalue()

	def __get_transcribe_file_location(self, file_uri:str, transcribe_client, job_name:str="Transcribe") ->str:
		"""Transcribe and return result location. 

		Args:
			file_uri (str): s3 path to audio file.
			transcribe_client (_type_): boto3 transcribe client.
			job_name (str, optional): Name of amazon AWS job. Defaults to "Transcribe".
		"""		
		transcribe_client.start_transcription_job(
			TranscriptionJobName = job_name,
			Media = {
				'MediaFileUri': file_uri
			},
			MediaFormat = get_extention_of_file_name(file_uri)[1:],
			LanguageCode = self.LANGUAGE_CODE
		)

		max_tries = 60
		while max_tries > 0:
			max_tries -= 1
			job = transcribe_client.get_transcription_job(TranscriptionJobName = job_name)
			job_status = job['TranscriptionJob']['TranscriptionJobStatus']
			if job_status in ['COMPLETED', 'FAILED']:
				# print(f"Job {job_name} is {job_status}.")
				if job_status == 'COMPLETED':
					download_uri:str = job['TranscriptionJob']['Transcript']['TranscriptFileUri']
				break
			else:
				# print(f"Waiting for {job_name}. Current status is {job_status}.")
				pass
			time.sleep(10)
		return download_uri