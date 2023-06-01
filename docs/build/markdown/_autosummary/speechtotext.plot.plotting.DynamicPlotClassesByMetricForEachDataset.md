# speechtotext.plot.plotting.DynamicPlotClassesByMetricForEachDataset


### _class_ DynamicPlotClassesByMetricForEachDataset(df, report_folder, file_name)
Bases: [`BaseResult`](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)

Dynamically create plot classes for each metric for each dataset in the given dataframe. This class is a parent class. The child class should be added to Plotting.CUSTOM_PLOTS.

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

#### _abstract_ create_plot()
Method that creates the plot.


#### create_plot_classes()
Creates plot classes.


#### save()
Saves plot to folder.
