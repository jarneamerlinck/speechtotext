# speechtotext metric package

## metrics

Module that calculates the metrics for speechtotext models.

Use this module like this:

```python
# Imports
from speechtotext.metric.metrics import Metrics

# Create metrics
m = Metrics("De stoel heeft krassen gemaakt op de vloer!", "De stoel heeft krassen gemaakt op de vloer", "id_from_dataset")
print(m)
```


### _class_ speechtotext.metric.metrics.Metrics(reference: str, hypothesis: str, audio_id: str, with_cleaning=True)
Bases: `object`

Class to calulate the metrics.
.. attribute:: class_attribute

> (class attribute) The class attribute.


> * **type**

>     str



#### wer()
(class attribute) word error rate (WER).


* **Type**

    float



#### mer()
(class attribute) match error rate (MER).


* **Type**

    float



#### wil()
(class attribute) word information lost (WIL).


* **Type**

    float



#### wip()
(class attribute) word information preserved (WIP).


* **Type**

    float



#### cer()
(class attribute) character error rate (CER).


* **Type**

    float



### speechtotext.metric.metrics.notebook_metrics_print(dataset: [Dataset](../datasets.md#speechtotext.datasets.Dataset), id: str, hypothesis: str)
Print metrics from transcript and hypothesis.


* **Parameters**

    
    * **dataset** ([*Dataset*](../datasets.md#speechtotext.datasets.Dataset)) – dataset of audio.


    * **id** (*str*) – id of the audio file.


    * **hypothesis** (*str*) – hypothesis transcript.


## customMetrics

Module to create custom metrics to save with the plots from the plotting module.

Use this module like this:

```python
# Imports
from speechtotext.functions import BaseResult
from speechtotext.plot.plotting import Plotting

# Create class with matplotlib picture
class BenchmarkResults(BaseMetrics):
        def create_df(self) -> pd.core.frame.DataFrame:
                return self.df

# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(BenchmarkResults)
```


### _class_ speechtotext.metric.customMetrics.BaseMetrics(df: DataFrame, report_folder: str, file_name: str)
Bases: [`BaseResult`](../functions.md#speechtotext.functions.BaseResult)

Base class used to create metrics for result dataframe.


#### _abstract_ create_df()
Creates df that needs to be saved.


* **Returns**

    Dataframe that needs to be saved.



* **Return type**

    pd.core.frame.DataFrame



#### save()
Saves Result to report folder.


### _class_ speechtotext.metric.customMetrics.BenchmarkResults(df: DataFrame, report_folder: str, file_name: str)
Bases: `BaseMetrics`

This class saves the results of the benchmark.


#### create_df()
Creates df that needs to be saved.


* **Returns**

    Dataframe that needs to be saved.



* **Return type**

    pd.core.frame.DataFrame



### _class_ speechtotext.metric.customMetrics.DefaultMetrics(df: DataFrame, report_folder: str, file_name: str)
Bases: `BaseMetrics`

This class calulates the default statistic metrics on the benchmark results.


#### create_df()
Creates df that needs to be saved.


* **Returns**

    Dataframe that needs to be saved.



* **Return type**

    pd.core.frame.DataFrame
