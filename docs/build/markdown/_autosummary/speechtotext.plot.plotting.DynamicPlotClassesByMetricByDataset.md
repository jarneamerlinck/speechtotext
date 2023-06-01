# speechtotext.plot.plotting.DynamicPlotClassesByMetricByDataset


### _class_ DynamicPlotClassesByMetricByDataset(df, report_folder, file_name)
Bases: [`BaseResult`](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)

Dynamically create plot classes for each metric for each database in the given dataframe. This class is a parent class. The child class should be added to Plotting.CUSTOM_PLOTS.

Creates object of class.


* **Parameters**

    
    * **df** (*pd.core.frame.DataFrame*) – Dataframe that needs to be plotted.


    * **report_folder** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to report folder.


    * **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Name of plot.


### Methods

| `create_plot`

 | 

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
