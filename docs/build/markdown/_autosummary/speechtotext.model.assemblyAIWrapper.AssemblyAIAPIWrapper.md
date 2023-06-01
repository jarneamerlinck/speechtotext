# speechtotext.model.assemblyAIWrapper.AssemblyAIAPIWrapper


### _class_ AssemblyAIAPIWrapper(model_version)
Bases: [`ModelWrapper`](speechtotext.model.modelWrapper.ModelWrapper.md#speechtotext.model.modelWrapper.ModelWrapper)

Wrapper for assemblyAi API. ASSEMBLY_AI_API_KEY needs to be in the ‘.env’ file in current directory.

Wrapper for assemblyAi model.


* **Parameters**

    **model_version** (*assemblyAiAPIVersion*) – Model version of assemblyAi STT API to use.


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

| `API_URL`
                                 | Connection url for the API.

                                                                    |
| `LANGUAGE_CODE`
                           | Code for the language to transcribe.

                                                           |
| `PATH_OF_TEMP_CONVERTED_AUDIO_FILE`
       | path to temp file that will be created to convert the audio files to an accepted audio format.

 |
| `POLLING_ENDPOINT`
                        | Polling endpoint url.

                                                                          |
| `TIME_SLEEP`
                              | Time to sleep after each polling.

                                                              |
| `TRANSCRIPT_ENDPOINT`
                     | Transcribe endpoint url.

                                                                       |
| `UPLOAD_ENDPOINT`
                         | Upload endpoint url.

                                                                           |

#### API_URL(_: [`str`](https://docs.python.org/3/library/stdtypes.html#str_ _ = 'https://api.assemblyai.com/v2/upload_ )
Connection url for the API.


* **Type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### LANGUAGE_CODE(_: [`str`](https://docs.python.org/3/library/stdtypes.html#str_ _ = 'nl_ )
Code for the language to transcribe.

See  [supported languages for assemblyAi](https://www.assemblyai.com/docs/#supported-languages)


* **Type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### PATH_OF_TEMP_CONVERTED_AUDIO_FILE(_: [`str`](https://docs.python.org/3/library/stdtypes.html#str_ _ = 'converted_audio_file.wav_ )
path to temp file that will be created to convert the audio files to an accepted audio format.


* **Type**

    PATH_OF_TEMP_CONVERTED_AUDIO_FILE



#### POLLING_ENDPOINT(_: [`str`](https://docs.python.org/3/library/stdtypes.html#str_ _ = 'https://api.assemblyai.com/v2/transcript/_ )
Polling endpoint url.


* **Type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### TIME_SLEEP(_: [`int`](https://docs.python.org/3/library/functions.html#int_ _ = _ )
Time to sleep after each polling.


* **Type**

    [int](https://docs.python.org/3/library/functions.html#int)



#### TRANSCRIPT_ENDPOINT(_: [`str`](https://docs.python.org/3/library/stdtypes.html#str_ _ = 'https://api.assemblyai.com/v2/transcript_ )
Transcribe endpoint url.


* **Type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### UPLOAD_ENDPOINT(_: [`str`](https://docs.python.org/3/library/stdtypes.html#str_ _ = 'https://api.assemblyai.com/v2/upload_ )
Upload endpoint url.


* **Type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



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



#### _clean_output(paragraphs)
Transcript list to 1 string.


* **Parameters**

    **paragraphs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – Transcript list.



* **Returns**

    Transcript.



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### _get_paragraphs(polling_endpoint, header)
Get results from polling endpoint.


* **Parameters**

    
    * **polling_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Polling endpoint.


    * **header** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – Http header.



* **Returns**

    Transcript of audio file in list.



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)



#### _make_polling_endpoint(transcript_response)
Make polling endoint.


* **Parameters**

    **transcript_response** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – Transcript response.



* **Returns**

    Polling endpoint.



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### _read_file_with_chunck_size(audio_file_name, chunk_size=5242880)
Read data from file.


* **Parameters**

    
    * **audio_file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to audio file.


    * **chunk_size** ([*int*](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Size of chunk. Defaults to 5242880.



* **Yields**

    *generator* – Audio file.



#### _request_transcript(upload_url, header)
Request transcript.


* **Parameters**

    
    * **upload_url** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – Url for request.


    * **header** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – Http header.



* **Returns**

    Response of request.



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### _upload_file(audio_file_name, header)
Upload file.


* **Parameters**

    
    * **audio_file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to audio file.


    * **header** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – Http header.



* **Returns**

    Url for request.



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### _wait_for_completion(polling_endpoint, header)
Wait for the translation to be done.


* **Parameters**

    
    * **polling_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Polling endpoint.


    * **header** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – Http header.



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
