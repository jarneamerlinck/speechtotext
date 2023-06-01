# speechtotext.plot.customPlots.DynamicallyByModelNameByDataset


### _class_ DynamicallyByModelNameByDataset(df, report_folder, file_name)
Bases: [`DynamicPlotClassesByMetricByDataset`](speechtotext.plot.plotting.DynamicPlotClassesByMetricByDataset.md#speechtotext.plot.plotting.DynamicPlotClassesByMetricByDataset)

Class that is used to create plots for an benchmark.

Creates object of class.


* **Parameters**

    
    * **df** (*pd.core.frame.DataFrame*) – Dataframe that needs to be plotted.


    * **report_folder** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to report folder.


    * **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Name of plot.


### Methods

| `create_plot`

 | 
* **rtype**

    `Figure`



 |
| `create_plot_classes`

                     | Creates plot classes.

                                                                          |
| `save`

                                    | Saves plot to folder.

                                                                          |

#### create_plot_classes()
Creates plot classes.


#### save()
Saves plot to folder.
