# speechtotext.plot.customPlots.MetricHeatMap


### _class_ MetricHeatMap(df, report_folder, file_name)
Bases: [`BaseMatPlotLib`](speechtotext.plot.plotting.BaseMatPlotLib.md#speechtotext.plot.plotting.BaseMatPlotLib)

Class that is used to create plots for an benchmark.

Creates object of BasePlot.


* **Parameters**

    
    * **df** (*pd.core.frame.DataFrame*) – Dataframe that needs to be plotted.


    * **report_folder** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to report folder.


    * **plot_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Name of plot.


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
