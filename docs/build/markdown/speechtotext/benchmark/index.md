# speechtotext benchmark package

## benchmarks

Module for benchmarks of speechtotext.

Use this module like this:

```python
# Imports
from speechtotext.datasets import Dataset
from speechtotext.benchmark.benchmarks import *

# Settings
number_of_samples = 10
report_name = "report name"
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
Benchmark.set_dataset(dataset)

# Create benchmark
wb = WhisperBenchmark()

# Run benchmark
wb(number_of_samples)

# Convert metrics to pandas dataframe
df = wb.convert_to_pandas()
print(df)

# Save metrics to csv (saves with datetime in name)
benchmark_results_to_csv([wb])

# Run benchmarks
## Settings
number_of_samples = 5
benchmark_dataset = dataset_RDH
benchmark_class_list: list[Benchmark] = [WhisperBenchmark, WhisperAPIBenchmark]

# Run benchmarks
results = run_benchmarks(benchmark_class_list, benchmark_dataset, number_of_samples, report_name)
```


### _class_ speechtotext.benchmark.benchmarks.Benchmark(with_cleaning=True)
Bases: `ABC`

Benchmark is used to test/validate an model.
Parent class for all benchmark classes.


#### BENCHMARK_SAMPLES(_: [Dataset](../index.md#speechtotext.datasets.Dataset_ _ = Non_ )
Dataset samples.


* **Type**

    [Dataset](../index.md#speechtotext.datasets.Dataset)



#### DATASET(_: [Dataset](../index.md#speechtotext.datasets.Dataset_ _ = Non_ )
Original dataset.


* **Type**

    [Dataset](../index.md#speechtotext.datasets.Dataset)



#### ERROR_LIST(_: list[pandas.core.frame.DataFrame_ _ = [_ )
List of errors.


* **Type**

    list[pd.core.frame.DataFrame]



#### \__call__(number_of_samples: int, with_cleaning=True)
Benchmark n samples.benchmark_results_to_csv


* **Parameters**

    
    * **number_of_samples** (*int*) – Number of samples to benchmark.


    * **with_cleaning** (*bool**, **optional*) – Set True to clean transcripts. Defaults to True.



#### convert_to_pandas()
Convert metrics to dataframe.


* **Returns**

    Pandas dataframe.



* **Return type**

    pd.core.frame.DataFrame



#### _abstract_ create_models()
Creates an list of ModelWrappers.


* **Returns**

    List of model wrappers.



* **Return type**

    list[[ModelWrapper](../model/index.md#speechtotext.model.modelWrapper.ModelWrapper)]



#### save_to_csv(save_name: str)
Save outputs of benchmark to csv.


* **Parameters**

    **save_name** (*str*) – Filename of output.



#### _classmethod_ set_dataset(dataset: [Dataset](../index.md#speechtotext.datasets.Dataset))
Set dataset for Benchmark class.


* **Parameters**

    **dataset** ([*Dataset*](../index.md#speechtotext.datasets.Dataset)) – Dataset to use with benchmark.



#### _classmethod_ update_samples(number_of_samples: int)
Update the sample dataset.


* **Parameters**

    **number_of_samples** (*int*) – Number of samples.



### speechtotext.benchmark.benchmarks.run_benchmarks(benchmark_class_list: list[speechtotext.benchmark.benchmarks.Benchmark], benchmark_dataset: [Dataset](../index.md#speechtotext.datasets.Dataset), number_of_samples: int, report_name: str)
Run al benchmarks out of list.


* **Parameters**

    
    * **benchmark_list** (*list**[**Benchmark**]*) – List of benchmark classes to run.


    * **dataset** ([*Dataset*](../index.md#speechtotext.datasets.Dataset)) – Dataset to use for benchmark.


    * **number_of_samples** (*int*) – Number of samples used in benchmark.


    * **report_name** (*str*) – Name of report. To save the errors to.


## customBenchmarks

Module for benchmarks of speechtotext.

Use this module like this:

```python
# Imports
from speechtotext.datasets import Dataset
from speechtotext.benchmark.benchmarks import *

# Settings
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
Benchmark.set_dataset(dataset)

# Create benchmark
wb = WhisperBenchmark()

# Run benchmark
wb(number_of_samples)

# Convert metrics to pandas dataframe
df = wb.convert_to_pandas()
print(df)

# Save metrics to csv (saves with datetime in name)
benchmark_results_to_csv([wb])
```


### _class_ speechtotext.benchmark.customBenchmarks.AmazonAPIBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for Amazon API transcribe.


#### MODEL_BASE(_: st_ _ = 'AmazonAPI_ )
Name of base model.


* **Type**

    str



#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    List of model wrappers.



* **Return type**

    list[[ModelWrapper](../model/index.md#speechtotext.model.modelWrapper.ModelWrapper)]



### _class_ speechtotext.benchmark.customBenchmarks.AssemblyAIAPIBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for AssemblyAI API.


#### MODEL_BASE(_: st_ _ = 'AssemblyAIAPI_ )
Name of base model.


* **Type**

    str



#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    List of model wrappers.



* **Return type**

    list[[ModelWrapper](../model/index.md#speechtotext.model.modelWrapper.ModelWrapper)]



### _class_ speechtotext.benchmark.customBenchmarks.AzureAPIBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for Azure API.


#### MODEL_BASE(_: st_ _ = 'AzureAPI_ )
Name of base model.


* **Type**

    str



#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    List of model wrappers.



* **Return type**

    list[[ModelWrapper](../model/index.md#speechtotext.model.modelWrapper.ModelWrapper)]



### _class_ speechtotext.benchmark.customBenchmarks.DeepgramAPIBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for Deepgram API.


#### MODEL_BASE(_: st_ _ = 'DeepgramAPI_ )
Name of base model.


* **Type**

    str



#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    List of model wrappers.



* **Return type**

    list[[ModelWrapper](../model/index.md#speechtotext.model.modelWrapper.ModelWrapper)]



### _class_ speechtotext.benchmark.customBenchmarks.GoogleAPIBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for Google API transcribe.


#### MODEL_BASE(_: st_ _ = 'GoogleAPI_ )
Name of base model.


* **Type**

    str



#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    List of model wrappers.



* **Return type**

    list[[ModelWrapper](../model/index.md#speechtotext.model.modelWrapper.ModelWrapper)]



### _class_ speechtotext.benchmark.customBenchmarks.SpeechmaticsAPIBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for Speechmatics API.


#### MODEL_BASE(_: st_ _ = 'SpeechmaticsAPI_ )
Name of base model.


* **Type**

    str



#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    List of model wrappers.



* **Return type**

    list[[ModelWrapper](../model/index.md#speechtotext.model.modelWrapper.ModelWrapper)]



### _class_ speechtotext.benchmark.customBenchmarks.WhisperAPIBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for API whisper models.


#### MODEL_BASE(_: st_ _ = 'WhisperAPI_ )
Name of base model.


* **Type**

    str



#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    List of model wrappers.



* **Return type**

    list[[ModelWrapper](../model/index.md#speechtotext.model.modelWrapper.ModelWrapper)]



### _class_ speechtotext.benchmark.customBenchmarks.WhisperBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for local whisper models.


#### MODEL_BASE(_: st_ _ = 'Whisper_ )
Name of base model.


* **Type**

    str



#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    List of model wrappers.



* **Return type**

    list[[ModelWrapper](../model/index.md#speechtotext.model.modelWrapper.ModelWrapper)]
