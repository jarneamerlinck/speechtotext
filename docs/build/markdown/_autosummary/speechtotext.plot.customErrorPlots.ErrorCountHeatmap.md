# speechtotext.plot.customErrorPlots.ErrorCountHeatmap


### _class_ ErrorCountHeatmap(df, report_folder, file_name)
Bases: [`BasePlotly`](speechtotext.plot.plotting.BasePlotly.md#speechtotext.plot.plotting.BasePlotly)

Class that is used to create error plots for an benchmark.

Creates object of BasePlot.


* **Parameters**

    
    * **df** (*pd.core.frame.DataFrame*) – Dataframe that needs to be plotted.


    * **report_folder** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to report folder.


    * **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Name of plot.


### Methods

| `create_plot`

 | Creates plot to be saved.

 |
| `save`

                                    | Saves plot to folder.

                                                                          |

#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



#### save()
Saves plot to folder.
