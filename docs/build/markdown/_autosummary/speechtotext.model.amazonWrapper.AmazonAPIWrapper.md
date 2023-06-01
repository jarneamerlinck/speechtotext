# speechtotext.model.amazonWrapper.AmazonAPIWrapper


### _class_ AmazonAPIWrapper(model_version)
Bases: [`ModelWrapper`](speechtotext.model.modelWrapper.ModelWrapper.md#speechtotext.model.modelWrapper.ModelWrapper)

Wrapper for AMAZON API. AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AMAZON_REGION and AMAZON_BUCKET need to be in the ‘.env’ file in current directory.

Wrapper for AMAZON model.


* **Parameters**

    **model_version** ([*AmazonAPIVersion*](speechtotext.model.amazonWrapper.AmazonAPIVersion.md#speechtotext.model.amazonWrapper.AmazonAPIVersion)) – Model version of AMAZON STT API to use.


### Methods

| `benchmark_n_samples`

 | Benchmark n samples with model.

 |
| `benchmark_sample`

                        | Benchmark sample with model.

                                                               |
| `benchmark_samples`

                       | Benchmark samples with model.

                                                              |
| `convert_sample`

                          | Convert sample to correct format.

                                                          |
| `get_model`

                               | Get model.

                                                                                 |
| `get_transcript_of_file`

                  | 

                                                                                           |
### Attributes

| `BUCKET_EXIST`
                            | Boolean that represents if the bucket exists.

                                              |
| `LANGUAGE_CODE`
                           | Code for the language to transcribe.

                                                       |
| `PATH_OF_TEMP_CONVERTED_AUDIO_FILE`
       | path to temp file that will be created to convert the audio files to an accepted audio format.

 |

#### BUCKET_EXIST(_: [`bool`](https://docs.python.org/3/library/functions.html#bool_ _ = Tru_ )
Boolean that represents if the bucket exists.


* **Type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### LANGUAGE_CODE(_: [`str`](https://docs.python.org/3/library/stdtypes.html#str_ _ = 'nl-NL_ )
Code for the language to transcribe.

See  [supported languages for amazon](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html)


* **Type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### PATH_OF_TEMP_CONVERTED_AUDIO_FILE(_: [`str`](https://docs.python.org/3/library/stdtypes.html#str_ _ = 'converted_audio_file.wav_ )
path to temp file that will be created to convert the audio files to an accepted audio format.


* **Type**

    PATH_OF_TEMP_CONVERTED_AUDIO_FILE



#### _append_error(samples, audio_id, error)
Append error to model_errors.


* **Parameters**

    
    * **samples** ([*SampleDataset*](speechtotext.datasets.SampleDataset.md#speechtotext.datasets.SampleDataset)) – Dataset of audio.


    * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Id of failed sample.


    * **error** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Error message.



#### _benchmark_sample_with_time(dataset, audio_id, with_cleaning=True)
Benchmark sample for model with timer.


* **Parameters**

    
    * **dataset** ([*Dataset*](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Id of audio file.


    * **with_cleaning** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    Metrics of the transcript.



* **Return type**

    [Metrics](speechtotext.metric.metrics.Metrics.md#speechtotext.metric.metrics.Metrics)



#### _get_transcribe_file_location(file_uri, transcribe_client, job_name='Transcribe')
Transcribe and return result location.
:raises AmazonNoTranscriptReturned: Exception when API does not return an transcript.


* **Parameters**

    
    * **file_uri** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – S3 path to audio file.


    * **(****)** (*transcribe_client*) – Boto3 transcribe client.


    * **file_ext** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – File extention of audio file.


    * **job_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Name of amazon AWS job. Defaults to “Transcribe”.



* **Return type**

    [`str`](https://docs.python.org/3/library/stdtypes.html#str)



#### _get_transcript_from_json_uri(json_uri)
Get transcript from amazon transcribe json result.


* **Parameters**

    **json_uri** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Uri of the resulting json file.



* **Returns**

    Transcript of the audio.



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### benchmark_n_samples(dataset, number_of_samples, with_cleaning=True)
Benchmark n samples with model.


* **Parameters**

    
    * **dataset** ([*Dataset*](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **number_of_samples** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Number of random samples to benchmerk.


    * **with_cleaning** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    List of metrics for each sample.



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)



#### benchmark_sample(dataset, audio_id, with_cleaning=True)
Benchmark sample with model.


* **Parameters**

    
    * **dataset** ([*Dataset*](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Id of audio file.


    * **with_cleaning** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    Metrics of the transcript.



* **Return type**

    [Metrics](speechtotext.metric.metrics.Metrics.md#speechtotext.metric.metrics.Metrics)



#### benchmark_samples(samples, with_cleaning=True)
Benchmark samples with model.


* **Parameters**

    
    * **dataset** ([*Dataset*](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **number_of_samples** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Number of random samples to benchmerk.


    * **with_cleaning** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    List of metrics for each sample.



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)



#### convert_sample(path_to_sample)
Convert sample to correct format.


* **Parameters**

    
    * **path_to_sample** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to sample.


    * **override** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Override original file. Defaults to False.



* **Returns**

    Path to converted sample.



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### get_model()
Get model.
