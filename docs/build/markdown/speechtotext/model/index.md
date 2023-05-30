# speechtotext model package

## modelWrapper

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


### _class_ speechtotext.model.modelWrapper.MetaModelWrapper(name, bases, attrs)
Bases: `type`

Meta class for model wrapper.

Created to automaticly convert a sample before transcribing.


#### _static_ \__new__(cls, name, bases, attrs)
If the class has a ‘get_transcript_of_file’ method, wrap it


#### _static_ wrap(get_transcript_of_file)
Return a wrapped instance method


### _class_ speechtotext.model.modelWrapper.ModelVersion(value)
Bases: `Enum`

Enum for the Available models.


* **Parameters**

    **Enum** (*ModelVersion*) – Available models.



### _class_ speechtotext.model.modelWrapper.ModelWrapper(model_version: ModelVersion)
Bases: `ABC`

Abstract Wrapper for model.

If audio needs to be converted use convert_sample in get_transcript_of_file.


#### PATH_OF_TEMP_CONVERTED_AUDIO_FILE(_: st_ _ = 'converted_audio_file.wav_ )
path to temp file that will be created to convert the audio files to an accepted audio format.


* **Type**

    PATH_OF_TEMP_CONVERTED_AUDIO_FILE



#### _append_error(samples: [SampleDataset](../index.md#speechtotext.datasets.SampleDataset), audio_id: str, error: str)
Append error to model_errors.


* **Parameters**

    
    * **samples** ([*SampleDataset*](../index.md#speechtotext.datasets.SampleDataset)) – Dataset of audio.


    * **id** (*str*) – Id of failed sample.


    * **error** (*str*) – Error message.



#### _benchmark_sample_with_time(dataset: [Dataset](../index.md#speechtotext.datasets.Dataset), audio_id: str, with_cleaning=True)
Benchmark sample for model with timer.


* **Parameters**

    
    * **dataset** ([*Dataset*](../index.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **id** (*str*) – Id of audio file.


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    Metrics of the transcript.



* **Return type**

    [Metrics](../metric/index.md#speechtotext.metric.metrics.Metrics)



#### benchmark_n_samples(dataset: [Dataset](../index.md#speechtotext.datasets.Dataset), number_of_samples: int, with_cleaning=True)
Benchmark n samples with model.


* **Parameters**

    
    * **dataset** ([*Dataset*](../index.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **number_of_samples** (*int*) – Number of random samples to benchmerk.


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    List of metrics for each sample.



* **Return type**

    list



#### benchmark_sample(dataset: [Dataset](../index.md#speechtotext.datasets.Dataset), audio_id: str, with_cleaning=True)
Benchmark sample with model.


* **Parameters**

    
    * **dataset** ([*Dataset*](../index.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **id** (*str*) – Id of audio file.


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    Metrics of the transcript.



* **Return type**

    [Metrics](../metric/index.md#speechtotext.metric.metrics.Metrics)



#### benchmark_samples(samples: [SampleDataset](../index.md#speechtotext.datasets.SampleDataset), with_cleaning=True)
Benchmark samples with model.


* **Parameters**

    
    * **dataset** ([*Dataset*](../index.md#speechtotext.datasets.Dataset)) – Dataset of audio.


    * **number_of_samples** (*int*) – Number of random samples to benchmerk.


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



* **Returns**

    List of metrics for each sample.



* **Return type**

    list



#### convert_sample(path_to_sample: str)
Convert sample to correct format.


* **Parameters**

    
    * **path_to_sample** (*str*) – Path to sample.


    * **override** (*bool**, **optional*) – Override original file. Defaults to False.



* **Returns**

    Path to converted sample.



* **Return type**

    str



#### _abstract_ get_model()
Get model. Set self.model.


#### get_transcript_of_file(path_to_sample)

### _class_ speechtotext.model.modelWrapper._CombinedMeta(name, bases, attrs)
Bases: `MetaModelWrapper`, `ABCMeta`

Class combining the metaclasses: MetaModelWrapper and ABCMeta.


* **Parameters**

    
    * **MetaModelWrapper** (*type*) – Metaclass for the ModelWrapper.


    * **ABCMeta** (*type*) – Abstract Base Classes.


## whisperWrapper

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
# Add model to Plotting
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
Online whisper version.


### _class_ speechtotext.model.whisperWrapper.WhisperAPIWrapper(model_version: WhisperAPIVersion)
Bases: `ModelWrapper`

Wrapper for whisper API. OPENAI_ORGANIZATION and OPENAI_API_KEY need to be in .env file in current directory.


#### get_model()
Get model.


#### get_transcript_of_file(path_to_sample)

### _class_ speechtotext.model.whisperWrapper.WhisperVersion(value)
Bases: `ModelVersion`

Enum for the available Whisper models.


* **Parameters**

    **Enum** (*WhisperVersion*) – Available whisper models.



#### BASE(_ = 'base_ )
Base whisper version.


#### LARGE(_ = 'large_ )
Biggest whisper version.


#### MEDIUM(_ = 'medium_ )
Larger then Base whisper version.


#### SMALL(_ = 'small_ )
Second smallest whisper version.


#### TINY(_ = 'tiny_ )
Smallest whisper version.


### _class_ speechtotext.model.whisperWrapper.WhisperWrapper(model_version: WhisperVersion)
Bases: `ModelWrapper`

Wrapper for whisper model.


#### get_model()
Get model.


#### get_transcript_of_file(path_to_sample)
## amazonWrapper

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
Default model version.


### _class_ speechtotext.model.amazonWrapper.AmazonAPIWrapper(model_version: AmazonAPIVersion)
Bases: `ModelWrapper`

Wrapper for AMAZON API. AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AMAZON_REGION and AMAZON_BUCKET need to be in the ‘.env’ file in current directory.


#### BUCKET_EXIST(_: boo_ _ = Tru_ )
Boolean that represents if the bucket exists.


* **Type**

    bool



#### LANGUAGE_CODE(_: st_ _ = 'nl-NL_ )
Code for the language to transcribe.

See  [supported languages for amazon](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html)


* **Type**

    str



#### _get_transcribe_file_location(file_uri: str, transcribe_client, job_name: str = 'Transcribe')
Transcribe and return result location.
:raises AmazonNoTranscriptReturned: Exception when API does not return an transcript.


* **Parameters**

    
    * **file_uri** (*str*) – S3 path to audio file.


    * **(****)** (*transcribe_client*) – Boto3 transcribe client.


    * **file_ext** (*str*) – File extention of audio file.


    * **job_name** (*str**, **optional*) – Name of amazon AWS job. Defaults to “Transcribe”.



#### _get_transcript_from_json_uri(json_uri: str)
Get transcript from amazon transcribe json result.


* **Parameters**

    **json_uri** (*str*) – Uri of the resulting json file.



* **Returns**

    Transcript of the audio.



* **Return type**

    str



#### get_model()
Get model.


#### get_transcript_of_file(path_to_sample)

### speechtotext.model.amazonWrapper.amazon_delete_job(transcribe_client, job_name: str)
Deletes a transcription job. This also deletes the transcript associated with
the job.


* **Parameters**

    
    * **job_name** (*str*) – job name.


    * **transcribe_client** (*boto3.botocore.client.TranscribeService*) – transcribe client.


## googleWrapper

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
Default model version.


### _class_ speechtotext.model.googleWrapper.GoogleAPIWrapper(model_version: GoogleAPIVersion)
Bases: `ModelWrapper`

Wrapper for google API. GOOGLE_APPLICATION_CREDENTIALS needs to be in the ‘.env’ file in current directory.


#### LANGUAGE_CODE(_: st_ _ = 'nl-BE_ )
Code for the language to transcribe.

See  [supported languages for google](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages).


* **Type**

    str



#### get_model()
Get model.


#### get_transcript_of_file(path_to_sample)
## deepgramWrapper

Modelwrapper implemented for deepgram API.

DEEPGRAM_API_KEY needs to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.deepgramWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
deepgramWrapper = deepgramAPIVersion(deepgramAPIVersion.deepgram_DEFAULT)

# Get model
deepgramWrapper.get_model()

# Benchmark choisen sample
deepgramWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = deepgramWrapper.benchmark_n_samples(dataset, number_of_samples)
```


### _class_ speechtotext.model.deepgramWrapper.DeepgramAPIVersion(value)
Bases: `ModelVersion`

Enum for the available deepgram API models.


* **Parameters**

    **Enum** (*deepgramAPIVersion*) – Available whisper API models.



#### DEEPGRAM_DEFAULT(_ = 'general_ )
Default model version.


#### DEEPGRAM_ENHANCED(_ = 'general-enhanced_ )
Enhanced model version.


### _class_ speechtotext.model.deepgramWrapper.DeepgramAPIWrapper(model_version: DeepgramAPIVersion)
Bases: `ModelWrapper`

Wrapper for deepgram API. DEEPGRAM_API_KEY needs to be in the ‘.env’ file in current directory.


#### LANGUAGE_CODE(_: st_ _ = 'nl_ )
Code for the language to transcribe.

See  [supported languages for deepgram](https://deepgram.com/product/languages/)


* **Type**

    str



#### get_model()
Get model.


#### get_transcript_of_file(path_to_sample)
## assemblyAIWrapper

Modelwrapper implemented for assemblyAi API.

ASSEMBLY_AI_API_KEY needs to be in the ‘.env’.

Use this module like this:

```python
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
```


### _class_ speechtotext.model.assemblyAIWrapper.AssemblyAIAPIVersion(value)
Bases: `ModelVersion`

Enum for the available assemblyAi API models.


* **Parameters**

    **Enum** (*assemblyAiAPIVersion*) – Available whisper API models.



#### ASSEMBLYAI_DEFAULT(_ = 'default_ )
Default model version.


### _class_ speechtotext.model.assemblyAIWrapper.AssemblyAIAPIWrapper(model_version: AssemblyAIAPIVersion)
Bases: `ModelWrapper`

Wrapper for assemblyAi API. ASSEMBLY_AI_API_KEY needs to be in the ‘.env’ file in current directory.


#### API_URL(_: st_ _ = 'https://api.assemblyai.com/v2/upload_ )
Connection url for the API.


* **Type**

    str



#### LANGUAGE_CODE(_: st_ _ = 'nl_ )
Code for the language to transcribe.

See  [supported languages for assemblyAi](https://www.assemblyai.com/docs/#supported-languages)


* **Type**

    str



#### POLLING_ENDPOINT(_: st_ _ = 'https://api.assemblyai.com/v2/transcript/_ )
Polling endpoint url.


* **Type**

    str



#### TIME_SLEEP(_: in_ _ = _ )
Time to sleep after each polling.


* **Type**

    int



#### TRANSCRIPT_ENDPOINT(_: st_ _ = 'https://api.assemblyai.com/v2/transcript_ )
Transcribe endpoint url.


* **Type**

    str



#### UPLOAD_ENDPOINT(_: st_ _ = 'https://api.assemblyai.com/v2/upload_ )
Upload endpoint url.


* **Type**

    str



#### _clean_output(paragraphs: list)
Transcript list to 1 string.


* **Parameters**

    **paragraphs** (*list*) – Transcript list.



* **Returns**

    Transcript.



* **Return type**

    str



#### _get_paragraphs(polling_endpoint: str, header: dict)
Get results from polling endpoint.


* **Parameters**

    
    * **polling_endpoint** (*str*) – Polling endpoint.


    * **header** (*dict*) – Http header.



* **Returns**

    Transcript of audio file in list.



* **Return type**

    list



#### _make_polling_endpoint(transcript_response: dict)
Make polling endoint.


* **Parameters**

    **transcript_response** (*dict*) – Transcript response.



* **Returns**

    Polling endpoint.



* **Return type**

    str



#### _read_file_with_chunck_size(audio_file_name: str, chunk_size: int = 5242880)
Read data from file.


* **Parameters**

    
    * **audio_file_name** (*str*) – Path to audio file.


    * **chunk_size** (*int**, **optional*) – Size of chunk. Defaults to 5242880.



* **Yields**

    *generator* – Audio file.



#### _request_transcript(upload_url: dict, header: dict)
Request transcript.


* **Parameters**

    
    * **upload_url** (*dict*) – Url for request.


    * **header** (*dict*) – Http header.



* **Returns**

    Response of request.



* **Return type**

    dict



#### _upload_file(audio_file_name: str, header: dict)
Upload file.


* **Parameters**

    
    * **audio_file_name** (*str*) – Path to audio file.


    * **header** (*dict*) – Http header.



* **Returns**

    Url for request.



* **Return type**

    dict



#### _wait_for_completion(polling_endpoint: str, header: dict)
Wait for the translation to be done.


* **Parameters**

    
    * **polling_endpoint** (*str*) – Polling endpoint.


    * **header** (*dict*) – Http header.



#### get_model()
Get model.


#### get_transcript_of_file(path_to_sample)
## azureWrapper

Modelwrapper implemented for Azure STT API.

AZURE_SPEECH_KEY API and AZURE_SPEECH_REGION need to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.azureWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
azureWrapper = AzureAPIVersion(AzureAPIVersion.AZURE_DEFAULT)

# Get model
azureWrapper.get_model()

# Benchmark choisen sample
azureWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = azureWrapper.benchmark_n_samples(dataset, number_of_samples)
```


### _class_ speechtotext.model.azureWrapper.AzureAPIVersion(value)
Bases: `ModelVersion`

Enum for the available AZURE API models.
:param Enum: Available whisper API models.
:type Enum: AzureAPIVersion


#### AZURE_DEFAULT(_ = 'AzureApi_ )
Default model version.


### _class_ speechtotext.model.azureWrapper.AzureAPIWrapper(model_version: AzureAPIVersion)
Bases: `ModelWrapper`

Wrapper for AZURE API. AZURE_SPEECH_KEY API and AZURE_SPEECH_REGION need to be in the ‘.env’ file in current directory.


#### LANGUAGE_CODE(_: st_ _ = 'nl-BE_ )
Code for the language to transcribe.

See [supported languages for azure](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt)


* **Type**

    str



#### get_model()
Get model.


#### get_transcript_of_file(path_to_sample)

### _exception_ speechtotext.model.azureWrapper.AzureCancellation(message: str)
Bases: `Exception`

Exception when Azure gives an cancelation message.


### _exception_ speechtotext.model.azureWrapper.AzureNoMatch(message: str)
Bases: `Exception`

Exception when Azure finds not match.

## speechmaticsWrapper

Modelwrapper implemented for Speechmatics STT API.

**WARNING**: Package version speechmatics-python==1.6.4 is needed to run the script. Errors on 1.7.0

SPEECHMATICS_API_KEY needs to be in the ‘.env’ file in current directory.

Use this module like this:

```python
# Imports
from speechtotext.model.speechmaticsWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
speechmaticsWrapper = SpeechmaticsAPIVersion(SpeechmaticsAPIVersion.SPEECHMATICS_DEFAULT)

# Get model
speechmaticsWrapper.get_model()

# Benchmark choisen sample
speechmaticsWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = speechmaticsWrapper.benchmark_n_samples(dataset, number_of_samples)
```


### _class_ speechtotext.model.speechmaticsWrapper.SpeechmaticsAPIVersion(value)
Bases: `ModelVersion`

Enum for the available SPEECHMATICS API models.


* **Parameters**

    **Enum** (*SpeechmaticsAPIVersion*) – Available Speechmatic API models.



#### SPEECHMATICS_DEFAULT(_ = 'SpeechmaticsApi_ )
Default model version.


### _class_ speechtotext.model.speechmaticsWrapper.SpeechmaticsAPIWrapper(model_version: SpeechmaticsAPIVersion)
Bases: `ModelWrapper`

Wrapper for SPEECHMATICS API. SPEECHMATICS_API_KEY needs to be in the ‘.env’ file in current directory.


#### CONNECTION_URL(_: st_ _ = 'wss://eu2.rt.speechmatics.com/v2/_ )
Connection url for the API.


* **Type**

    str



#### LANGUAGE_CODE(_: st_ _ = 'nl_ )
Code for the language to transcribe.

See  [supported languages for speechmatics](https://docs.speechmatics.com/introduction/supported-languages).


* **Type**

    str



#### get_model()
Get model.


#### get_transcript_of_file(path_to_sample)
