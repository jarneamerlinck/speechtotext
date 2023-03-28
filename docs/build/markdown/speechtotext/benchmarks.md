# Benchmarks

## speechtotext.benchmarks module


### _class_ speechtotext.benchmarks.Benchmark(dataset: [Dataset](datasets.md#speechtotext.datasets.Dataset), with_cleaning=True)
Bases: `ABC`


#### convert_to_pandas()
convert metrics to dataframe


* **Returns**

    pandas dataframe



* **Return type**

    pd.core.frame.DataFrame



#### _abstract_ create_models()
Creates an list of ModelWrappers


* **Returns**

    list of model wrappers



* **Return type**

    list[[ModelWrapper](models/index.md#speechtotext.models.modelWrapper.ModelWrapper)]



#### save_to_csv(save_name: str)

### _class_ speechtotext.benchmarks.WhisperBenchmark(dataset: [Dataset](datasets.md#speechtotext.datasets.Dataset), with_cleaning=True)
Bases: `Benchmark`


#### MODEL_BASE(_ = 'Whisper_ )

#### create_models()
Creates an list of ModelWrappers


* **Returns**

    list of model wrappers



* **Return type**

    list[[ModelWrapper](models/index.md#speechtotext.models.modelWrapper.ModelWrapper)]
