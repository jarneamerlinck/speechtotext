# speechtotext.metric.customMetrics.ResultMetrics


### _class_ ResultMetrics(df, report_folder, file_name)
Bases: [`BaseMetrics`](speechtotext.metric.customMetrics.BaseMetrics.md#speechtotext.metric.customMetrics.BaseMetrics)

This class calulates the default statistic metrics on the benchmark results.

Creates object of BaseResult. Child class should be added to Plotting.CUSTOM_RESULTS.


* **Parameters**

    
    * **df** (*pd.core.frame.DataFrame*) – Dataframe that needs to be plotted.


    * **report_folder** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to report folder.


    * **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Name of saved File.


### Methods

| `create_df`

 | Creates df that needs to be saved.

 |
| `save`

                                    | Saves Result to report folder.

                                                   |

#### create_df()
Creates df that needs to be saved.


* **Returns**

    Dataframe that needs to be saved.



* **Return type**

    pd.core.frame.DataFrame



#### save()
Saves Result to report folder.
