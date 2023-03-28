# Speechtotext models package

## Submodules

## speechtotext.models.modelWrapper module


### _class_ speechtotext.models.modelWrapper.ModelVersion(value)
Bases: `Enum`

Enum for the availible models


* **Parameters**

    **Enum** (*ModelVersion*) – Availible models



### _class_ speechtotext.models.modelWrapper.ModelWrapper(model_version: ModelVersion)
Bases: `ABC`

Abstract Wrapper for model


#### benchmark_n_samples(dataset: [Dataset](../datasets.md#speechtotext.datasets.Dataset), number_of_samples: int, with_cleaning=True)
Benchmark n samples with model


* **Parameters**

    
    * **dataset** ([*Dataset*](../datasets.md#speechtotext.datasets.Dataset)) – Dataset of audio


    * **number_of_samples** (*int*) – Number of random samples to benchmerk


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    list of metrics for each sample



* **Return type**

    list



#### benchmark_sample(dataset: [Dataset](../datasets.md#speechtotext.datasets.Dataset), id: str, with_cleaning=True)
Benchmark sample with model


* **Parameters**

    
    * **dataset** ([*Dataset*](../datasets.md#speechtotext.datasets.Dataset)) – Dataset of audio


    * **id** (*str*) – Id of audio file


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    Metrics of the transcript



* **Return type**

    [Metrics](../metrics.md#speechtotext.metrics.Metrics)



#### benchmark_samples(samples: [SampleDataset](../datasets.md#speechtotext.datasets.SampleDataset), with_cleaning=True)
Benchmark samples with model


* **Parameters**

    
    * **dataset** ([*Dataset*](../datasets.md#speechtotext.datasets.Dataset)) – Dataset of audio


    * **number_of_samples** (*int*) – Number of random samples to benchmerk


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    list of metrics for each sample



* **Return type**

    list



#### _abstract_ get_model()
Get model. Set self.model


#### _abstract_ get_transcript_of_file(audio_file_name: str)
Get transcript of audio file


* **Parameters**

    **audio_file_name** (*str*) – Path to audio file



* **Returns**

    Transcript of audio file



* **Return type**

    str


## speechtotext.models.whisperWrapper module


### _class_ speechtotext.models.whisperWrapper.WhisperVersion(value)
Bases: `ModelVersion`

Enum for the available Whisper models


* **Parameters**

    **Enum** (*WhisperModel*) – Available whisper models



#### BASE(_ = 'base_ )

#### LARGE(_ = 'large_ )

#### MEDIUM(_ = 'medium_ )

#### SMALL(_ = 'small_ )

#### TINY(_ = 'tiny_ )

### _class_ speechtotext.models.whisperWrapper.WhisperWrapper(model_version: WhisperVersion)
Bases: `ModelWrapper`

Wrapper for whisper model


#### MODEL_DIR(_ = 'models/whisper_ )

#### get_model()
Get model


#### get_transcript_of_file(audio_file_name: str)
Get transcript of audio file


* **Parameters**

    **audio_file_name** (*str*) – Path to audio file



* **Returns**

    Transcript of audio file



* **Return type**

    str
