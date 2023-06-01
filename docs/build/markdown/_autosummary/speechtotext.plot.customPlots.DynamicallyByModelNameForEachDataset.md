# speechtotext.plot.customPlots.DynamicallyByModelNameForEachDataset


### _class_ DynamicallyByModelNameForEachDataset(df, report_folder, file_name)
Bases: [`DynamicPlotClassesByMetricForEachDataset`](speechtotext.plot.plotting.DynamicPlotClassesByMetricForEachDataset.md#speechtotext.plot.plotting.DynamicPlotClassesByMetricForEachDataset)

Class that is used to create plots for an benchmark.

Creates object of class.


* **Parameters**

    
    * **df** (*pd.core.frame.DataFrame*) – Dataframe that needs to be plotted.


    * **report_folder** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to report folder.


    * **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Name of plot.


### Methods

| `create_plot`

 | Method that creates the plot.

 |
| `create_plot_classes`

                     | Creates plot classes.

                                                                          |
| `save`

                                    | Saves plot to folder.

                                                                          |

#### create_plot()
Method that creates the plot.


* **Return type**

    `Figure`



#### create_plot_classes()
Creates plot classes.


#### save()
Saves plot to folder.
