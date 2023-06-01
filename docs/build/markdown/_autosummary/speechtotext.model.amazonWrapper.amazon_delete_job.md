# speechtotext.model.amazonWrapper.amazon_delete_job


### amazon_delete_job(transcribe_client, job_name)
Deletes a transcription job. This also deletes the transcript associated with
the job.


* **Parameters**

    
    * **job_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – job name.


    * **transcribe_client** (*boto3.botocore.client.TranscribeService*) – transcribe client.
