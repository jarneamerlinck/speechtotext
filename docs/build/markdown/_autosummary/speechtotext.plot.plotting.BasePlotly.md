# speechtotext.plot.plotting.BasePlotly


### _class_ BasePlotly(df, report_folder, file_name)
Bases: [`BaseResult`](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)

Parent class for custom plots with Plotly. Code can be generated from d-tale.
Child class should be made and added to Plotting.CUSTOM_RESULTS, Plotting.CUSTOM_ERRORS, Plotting.CUSTOM_PLOTS or Plotting.CUSTOM_ERROR_PLOTS

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

#### _abstract_ create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



#### save()
Saves plot to folder.
