# Benchmarks

## speechtotext.benchmarks module

Module for benchmarks of speech2text.

Use this module like this:

```python
# Imports
from speechtotext.datasets import Dataset
from speechtotext.benchmarks import *

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


### _class_ speechtotext.benchmarks.Benchmark(with_cleaning=True)
Bases: `ABC`

Benchmark is used to test/validate an model.
Parent class for all benchmark classes.


#### BENCHMARK_SAMPLES()
Dataset with just samples that is shared for the child classes.


* **Type**

    [SampleDataset](datasets.md#speechtotext.datasets.SampleDataset)



#### DATASET()
Dataset that is shared for the child classes.


* **Type**

    [Dataset](datasets.md#speechtotext.datasets.Dataset)



#### BENCHMARK_SAMPLES(_: [Dataset](datasets.md#speechtotext.datasets.Dataset_ _ = Non_ )

#### DATASET(_: [Dataset](datasets.md#speechtotext.datasets.Dataset_ _ = Non_ )

#### convert_to_pandas()
convert metrics to dataframe.


* **Returns**

    pandas dataframe.



* **Return type**

    pd.core.frame.DataFrame



#### _abstract_ create_models()
Creates an list of ModelWrappers.


* **Returns**

    list of model wrappers.



* **Return type**

    list[[ModelWrapper](models/index.md#speechtotext.models.modelWrapper.ModelWrapper)]



#### save_to_csv(save_name: str)
save outputs of benchmark to csv.


* **Parameters**

    **save_name** (*str*) – filename of output.



#### _classmethod_ set_dataset(dataset: [Dataset](datasets.md#speechtotext.datasets.Dataset))
Set dataset for Benchmark class.


* **Parameters**

    **dataset** ([*Dataset*](datasets.md#speechtotext.datasets.Dataset)) – Dataset to use with benchmark.



#### _classmethod_ update_samples(number_of_samples: int)
Update the sample dataset.


* **Parameters**

    **number_of_samples** (*int*) – Number of samples.



### _class_ speechtotext.benchmarks.WhisperAPIBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for API whisper models.


#### MODEL_BASE(_ = 'WhisperAPI_ )

#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    list of model wrappers.



* **Return type**

    list[[ModelWrapper](models/index.md#speechtotext.models.modelWrapper.ModelWrapper)]



### _class_ speechtotext.benchmarks.WhisperBenchmark(with_cleaning=True)
Bases: `Benchmark`

Benchmark for local whisper models.


#### MODEL_BASE(_ = 'Whisper_ )

#### create_models()
Creates an list of ModelWrappers.


* **Returns**

    list of model wrappers.



* **Return type**

    list[[ModelWrapper](models/index.md#speechtotext.models.modelWrapper.ModelWrapper)]



### speechtotext.benchmarks.benchmark_results_to_csv(results: list[pandas.core.frame.DataFrame], save_name: str = 'benchmark_results_2023-03-29_11-44-01.csv')
results (list[pd.core.frame.DataFrame]): List of results.


* **Parameters**

    
    * **results** (*list**[**pd.core.frame.DataFrame**]*) – List of results from benchmarks.


    * **save_name** (*str**, **optional*) – filename of output. Defaults to DEFAULT_CSV_NAME.
