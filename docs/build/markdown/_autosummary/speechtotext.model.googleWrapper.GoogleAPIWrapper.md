# speechtotext.model.googleWrapper.GoogleAPIWrapper


### _class_ GoogleAPIWrapper(model_version)
Bases: [`ModelWrapper`](speechtotext.model.modelWrapper.ModelWrapper.md#speechtotext.model.modelWrapper.ModelWrapper)

Wrapper for google API. GOOGLE_APPLICATION_CREDENTIALS needs to be in the ‘.env’ file in current directory.

Wrapper for google model.


* **Parameters**

    **model_version** (*googleAPIVersion*) – Model version of google STT API to use.


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

| `LANGUAGE_CODE`
                           | Code for the language to transcribe.

                                                           |
| `PATH_OF_TEMP_CONVERTED_AUDIO_FILE`
       | path to temp file that will be created to convert the audio files to an accepted audio format.

 |

#### LANGUAGE_CODE(_: [`str`](https://docs.python.org/3/library/stdtypes.html#str_ _ = 'nl-BE_ )
Code for the language to transcribe.

See  [supported languages for google](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages).


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
