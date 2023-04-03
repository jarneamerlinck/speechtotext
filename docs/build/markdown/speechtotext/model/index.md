# Speechtotext model package

## speechtotext.model.modelWrapper

Module with the parent classes for the model wrapper. Needs to be implemented to use the benchmarks.

Use this module like this:

```python
# Imports
from speechtotext.model.moduleWrapper import *
from speechtotext.benchmark.benchmarks import *
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


### _class_ speechtotext.model.modelWrapper.ModelVersion(value)
Bases: `Enum`

Enum for the availible models.


* **Parameters**

    **Enum** (*ModelVersion*) – Availible models.



### _class_ speechtotext.model.modelWrapper.ModelWrapper(model_version: ModelVersion)
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

    [Metrics](../metric/index.md#speechtotext.metric.metrics.Metrics)



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


## speechtotext.model.whisperWrapper

Modelwrapper implemented for whisper. Local and API.

API OPENAI_API_KEY and OPENAI_ORGANIZATION need to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.whisperWrapper import *
from speechtotext.benchmark.benchmarks import *
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


### _class_ speechtotext.model.whisperWrapper.WhisperAPIVersion(value)
Bases: `ModelVersion`

Enum for the available Whisper API models.


* **Parameters**

    **Enum** (*WhisperAPIVersion*) – Available whisper API models.



#### WHISPER_1(_ = 'whisper-1_ )

### _class_ speechtotext.model.whisperWrapper.WhisperAPIWrapper(model_version: WhisperAPIVersion)
Bases: `ModelWrapper`

Wrapper for whisper API. OPENAI_ORGANIZATION and OPENAI_API_KEY need to be in .env file in current directory.


#### get_model()
Get model.


#### get_transcript_of_file(audio_file_name: str)
Get transcript of audio file with API call.


* **Parameters**

    **audio_file_name** (*str*) – Path to audio file.



* **Returns**

    Transcript of audio file.



* **Return type**

    str



### _class_ speechtotext.model.whisperWrapper.WhisperVersion(value)
Bases: `ModelVersion`

Enum for the available Whisper models.


* **Parameters**

    **Enum** (*WhisperVersion*) – Available whisper models.



#### BASE(_ = 'base_ )

#### LARGE(_ = 'large_ )

#### MEDIUM(_ = 'medium_ )

#### SMALL(_ = 'small_ )

#### TINY(_ = 'tiny_ )

### _class_ speechtotext.model.whisperWrapper.WhisperWrapper(model_version: WhisperVersion)
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


## speechtotext.model.amazonWrapper

Modelwrapper implemented for Amazon STT API.

AMAZON API. AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AMAZON_REGION and AMAZON_BUCKET  need to be in the ‘.env’.

Use this module like this:

```python
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
```


### _class_ speechtotext.model.amazonWrapper.AmazonAPIVersion(value)
Bases: `ModelVersion`

Enum for the available AMAZON API models. This is for the  [Custom language model](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_CreateLanguageModel.html).


* **Parameters**

    **Enum** (*AmazonAPIVersion*) – Available whisper API models.



#### AMAZON_DEFAULT(_ = 'AmazonApi_ )

### _class_ speechtotext.model.amazonWrapper.AmazonAPIWrapper(model_version: AmazonAPIVersion)
Bases: `ModelWrapper`

Wrapper for AMAZON API. AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AMAZON_REGION and AMAZON_BUCKET need to be in the ‘.env’ file in current directory.


#### LANGUAGE_CODE(_: st_ _ = 'nl-NL_ )

#### get_model()
Get model.


#### get_transcript_of_file(audio_file_name: str)
Get transcript of audio file with API call.


* **Parameters**

    **audio_file_name** (*str*) – Path to audio file.



* **Returns**

    Transcript of audio file.



* **Return type**

    str


## speechtotext.model.googleWrapper

Modelwrapper implemented for google STT API.

GOOGLE_APPLICATION_CREDENTIALS needs to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.googleWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
googleWrapper = googleAPIVersion(googleAPIVersion.google_DEFAULT)

# Get model
googleWrapper.get_model()

# Benchmark choisen sample
googleWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = googleWrapper.benchmark_n_samples(dataset, number_of_samples)
```


### _class_ speechtotext.model.googleWrapper.GoogleAPIVersion(value)
Bases: `ModelVersion`

Enum for the available google API models.


* **Parameters**

    **Enum** (*googleAPIVersion*) – Available whisper API models.



#### GOOGLE_DEFAULT(_ = 'googleApi_ )

### _class_ speechtotext.model.googleWrapper.GoogleAPIWrapper(model_version: GoogleAPIVersion)
Bases: `ModelWrapper`

Wrapper for google API. GOOGLE_APPLICATION_CREDENTIALS needs to be in the ‘.env’ file in current directory.


#### LANGUAGE_CODE(_: st_ _ = 'nl-BE_ )

#### get_model()
Get model.


#### get_transcript_of_file(audio_file_name: str)
Get transcript of audio file with API call.


* **Parameters**

    **audio_file_name** (*str*) – Path to audio file.



* **Returns**

    Transcript of audio file.



* **Return type**

    str
