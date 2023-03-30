# Speechtotext models package

## Submodules

## speechtotext.models.modelWrapper module

Module with the parent classes for the model wrapper. Needs to be implemented to use the benchmarks.

Use this module like this:

```python
# Imports
from speechtotext.models.moduleWrapper import *
from speechtotext.benchmarks import *
from speechtotext.datasets import Dataset

# Create child class for ModelVersion
class ChildModelVersion(ModelVersion):
        MODEL_VERSION   = "demo"

# Create child class for ModelWrapper
class ChildModelWrapper(ModelWrapper):
        def __init__(self, model_version:ChildModelVersion):

                self.model_version = model_version

        def get_model(self, model:modelType):
                self.model = model

        def get_transcript_of_file(self, audio_file_name:str) -> str:
                result = self.model.transcribe(audio_file_name)
                return result["text"]

# Create child class of benchmark
class ChildBenchmark(Benchmark):
        MODEL_BASE = "model_name"

        def create_models(self) -> list[ModelWrapper]:
                models = []
                for version in ChildModelVersion:
                        models.append(ChildModelWrapper(version))
                return models

# Create benchmark
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
Benchmark.set_dataset(dataset)

benchmark = ChildBenchmark()

# Run benchmark
benchmark(number_of_samples)
```


### _class_ speechtotext.models.modelWrapper.ModelVersion(value)
Bases: `Enum`

Enum for the availible models.


* **Parameters**

    **Enum** (*ModelVersion*) – Availible models.



### _class_ speechtotext.models.modelWrapper.ModelWrapper(model_version: ModelVersion)
Bases: `ABC`

Abstract Wrapper for model.


#### benchmark_n_samples(dataset: [Dataset](../datasets.md#speechtotext.datasets.Dataset), number_of_samples: int, with_cleaning=True)
Benchmark n samples with model.


* **Parameters**

    
    * **dataset** ([*Dataset*](../datasets.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **number_of_samples** (*int*) – Number of random samples to benchmerk.


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    list of metrics for each sample.



* **Return type**

    list



#### benchmark_sample(dataset: [Dataset](../datasets.md#speechtotext.datasets.Dataset), id: str, with_cleaning=True)
Benchmark sample with model.


* **Parameters**

    
    * **dataset** ([*Dataset*](../datasets.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **id** (*str*) – Id of audio file.


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    Metrics of the transcript.



* **Return type**

    [Metrics](../metrics.md#speechtotext.metrics.Metrics)



#### benchmark_samples(samples: [SampleDataset](../datasets.md#speechtotext.datasets.SampleDataset), with_cleaning=True)
Benchmark samples with model.


* **Parameters**

    
    * **dataset** ([*Dataset*](../datasets.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **number_of_samples** (*int*) – Number of random samples to benchmerk.


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    list of metrics for each sample.



* **Return type**

    list



#### _abstract_ get_model()
Get model. Set self.model.


#### _abstract_ get_transcript_of_file(audio_file_name: str)
Get transcript of audio file.


* **Parameters**

    **audio_file_name** (*str*) – Path to audio file.



* **Returns**

    Transcript of audio file.



* **Return type**

    str


## speechtotext.models.whisperWrapper module

Modelwrapper implemented for whisper. Local and API.

Use this module like this:

```python
# Imports
from speechtotext.models.whisperWrapper import *
from speechtotext.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
whisperWrapper = WhisperWrapper(WhisperVersion.TINY)

# Get model
whisperWrapper.get_model()

# Benchmark choisen sample
whisperWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = whisperWrapper.benchmark_n_samples(dataset, number_of_samples)
```


### _class_ speechtotext.models.whisperWrapper.WhisperAPIVersion(value)
Bases: `ModelVersion`

Enum for the available Whisper API models.


* **Parameters**

    **Enum** (*WhisperAPIVersion*) – Available whisper API models.



#### WHISPER_1(_ = 'whisper-1_ )

### _class_ speechtotext.models.whisperWrapper.WhisperAPIWrapper(model_version: WhisperAPIVersion)
Bases: `ModelWrapper`

Wrapper for whisper API. OPENAI_ORGANIZATION and OPENAI_API_KEY need to be in .env file in current directory.


#### get_model()
Get model


#### get_transcript_of_file(audio_file_name: str)
Get transcript of audio file with API call.


* **Parameters**

    **audio_file_name** (*str*) – Path to audio file.



* **Returns**

    Transcript of audio file.



* **Return type**

    str



### _class_ speechtotext.models.whisperWrapper.WhisperVersion(value)
Bases: `ModelVersion`

Enum for the available Whisper models.


* **Parameters**

    **Enum** (*WhisperVersion*) – Available whisper models.



#### BASE(_ = 'base_ )

#### LARGE(_ = 'large_ )

#### MEDIUM(_ = 'medium_ )

#### SMALL(_ = 'small_ )

#### TINY(_ = 'tiny_ )

### _class_ speechtotext.models.whisperWrapper.WhisperWrapper(model_version: WhisperVersion)
Bases: `ModelWrapper`

Wrapper for whisper model.


#### get_model()
Get model.


#### get_transcript_of_file(audio_file_name: str)
Get transcript of audio file.


* **Parameters**

    **audio_file_name** (*str*) – Path to audio file.



* **Returns**

    Transcript of audio file.



* **Return type**

    str
