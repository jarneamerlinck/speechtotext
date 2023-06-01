# speechtotext.benchmark.benchmarks.Benchmark


### _class_ Benchmark(with_cleaning=True)
Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Benchmark is used to test/validate an model.
Parent class for all benchmark classes.

Create benchmark object.


* **Parameters**

    **with_cleaning** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Clean. Defaults to True.


### Methods

| `convert_to_pandas`

 | Convert metrics to dataframe.

 |
| `create_models`

                           | Creates an list of ModelWrappers.

                           |
| `save_to_csv`

                             | Save outputs of benchmark to csv.

                           |
| `set_dataset`

                             | Set dataset for Benchmark class.

                            |
| `update_samples`

                          | Update the sample dataset.

                                  |
### Attributes

| `BENCHMARK_SAMPLES`
                       | Dataset samples.

                                            |
| `DATASET`
                                 | Original dataset.

                                           |
| `ERROR_LIST`
                              | List of errors.

                                             |

#### BENCHMARK_SAMPLES(_: [`Dataset`](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset_ _ = Non_ )
Dataset samples.


* **Type**

    [Dataset](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset)



#### DATASET(_: [`Dataset`](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset_ _ = Non_ )
Original dataset.


* **Type**

    [Dataset](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset)



#### ERROR_LIST(_: [`list`](https://docs.python.org/3/library/stdtypes.html#list)[`DataFrame`_ _ = [_ )
List of errors.


* **Type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)[pd.core.frame.DataFrame]



#### \__call__(number_of_samples, with_cleaning=True)
Benchmark n samples.benchmark_results_to_csv


* **Parameters**

    
    * **number_of_samples** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Number of samples to benchmark.


    * **with_cleaning** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Set True to clean transcripts. Defaults to True.



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

    [list](https://docs.python.org/3/library/stdtypes.html#list)[[ModelWrapper](speechtotext.model.modelWrapper.ModelWrapper.md#speechtotext.model.modelWrapper.ModelWrapper)]



#### save_to_csv(save_name)
Save outputs of benchmark to csv.


* **Parameters**

    **save_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Filename of output.



#### _classmethod_ set_dataset(dataset)
Set dataset for Benchmark class.


* **Parameters**

    **dataset** ([*Dataset*](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset)) – Dataset to use with benchmark.



#### _classmethod_ update_samples(cls, number_of_samples)
Update the sample dataset.


* **Parameters**

    **number_of_samples** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Number of samples.
