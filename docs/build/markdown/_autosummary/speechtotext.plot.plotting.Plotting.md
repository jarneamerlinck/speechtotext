# speechtotext.plot.plotting.Plotting


### _class_ Plotting(results, errors, report_name)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Class that is used to create plots for an benchmark.

Creates plotting object


* **Parameters**

    
    * **results** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**pd.core.frame.DataFrame**]*) – List of result dataframes.


    * **errors** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**pd.core.frame.DataFrame**]*) – List of error dataframes.


    * **report_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Name of report.


### Methods

| `launch_dtale`

 | Launch webui to explore the data.

 |
| `save_all`

                                 | Loops over all customPlot classes in CUSTOM_PLOTS to creates and saves the plots.

              |
### Attributes

| `CUSTOM_ERRORS`
                            | List of error classes that need to be saved.

                                                   |
| `CUSTOM_ERROR_PLOTS`
                       | List of error plot classes that need to be saved.

                                              |
| `CUSTOM_PLOTS`
                             | List of plot classes that need to be saved.

                                                    |
| `CUSTOM_RESULTS`
                           | List of result classes that need to be saved.

                                                  |
| `DATASET_NAMES`
                            | List of dataset names that were used for the benchmarks.

                                       |

#### CUSTOM_ERRORS(_: [`list`](https://docs.python.org/3/library/stdtypes.html#list)[[`BaseResult`](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)_ _ = [_ )
List of error classes that need to be saved.

This could be an pandas df, report text file, …


* **Type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseResult](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)]



#### CUSTOM_ERROR_PLOTS(_: [`list`](https://docs.python.org/3/library/stdtypes.html#list)[[`BaseResult`](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)_ _ = [<class 'speechtotext.plot.customErrorPlots.ErrorCountByModel'>, <class 'speechtotext.plot.customErrorPlots.ErrorCountByModelByDataset'>, <class 'speechtotext.plot.customErrorPlots.ErrorCountHeatmap'>_ )
List of error plot classes that need to be saved.

This could be an plotly, matplotlib or another plot.


* **Type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseResult](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)]



#### CUSTOM_PLOTS(_: [`list`](https://docs.python.org/3/library/stdtypes.html#list)[[`BaseResult`](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)_ _ = [<class 'speechtotext.plot.customPlots.DynamicallyByModelNameForEachDataset'>, <class 'speechtotext.plot.customPlots.DynamicallyByModelNameByDataset'>, <class 'speechtotext.plot.customPlots.MetricHeatMap'>_ )
List of plot classes that need to be saved.

This could be an plotly, matplotlib or another plot.


* **Type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseResult](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)]



#### CUSTOM_RESULTS(_: [`list`](https://docs.python.org/3/library/stdtypes.html#list)[[`BaseResult`](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)_ _ = [<class 'speechtotext.metric.customMetrics.BenchmarkResults'>, <class 'speechtotext.metric.customMetrics.ResultMetrics'>_ )
List of result classes that need to be saved.

This could be an pandas df, report text file, …


* **Type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseResult](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)]



#### DATASET_NAMES(_: [`list`](https://docs.python.org/3/library/stdtypes.html#list)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)_ _ = [_ )
List of dataset names that were used for the benchmarks.


* **Type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]



#### launch_dtale()
Launch webui to explore the data.


#### save_all()
Loops over all customPlot classes in CUSTOM_PLOTS to creates and saves the plots.
