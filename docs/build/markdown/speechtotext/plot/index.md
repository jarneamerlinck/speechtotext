# speechtotext plot package

## plotting

Module that plots the results from the benchmarks.

Use this module like this:

```python
# Imports
from speechtotext.plot.plotting import BasePlot, Plotting

# Create plotting object
plotting = Plotting(results=results, report_name = "report_name")

# Create all custom plots that are added to Plotting.CUSTOM_PLOTS
plotting.save_all()
```


### _class_ speechtotext.plot.plotting.BaseMatPlotLib(df: DataFrame, report_folder: str, file_name: str)
Bases: [`BaseResult`](../index.md#speechtotext.functions.BaseResult)

Parent class for custom plots with matplotlib. Child class should be made and added to Plotting.CUSTOM_RESULTS.


#### _abstract_ create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



#### save()
Saves plot to folder.


### _class_ speechtotext.plot.plotting.BasePlotly(df: DataFrame, report_folder: str, file_name: str)
Bases: [`BaseResult`](../index.md#speechtotext.functions.BaseResult)

Parent class for custom plots with Plotly. Code can be generated from d-tale. Child class should be made and added to Plotting.CUSTOM_RESULTS.


#### _abstract_ create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



#### save()
Saves plot to folder.


### _class_ speechtotext.plot.plotting.Plotting(results: list[pandas.core.frame.DataFrame], report_name: str)
Bases: `object`

Class that is used to create plots for an benchmark.


#### CUSTOM_RESULTS(_: list[[speechtotext.functions.BaseResult](../index.md#speechtotext.functions.BaseResult)_ _ = [<class 'speechtotext.metric.customMetrics.BenchmarkResults'>, <class 'speechtotext.metric.customMetrics.DefaultMetrics'>_ )

#### launch_dtale()
Launch webui to explore the data.


#### save_all()
Loops over all customPlot classes in CUSTOM_PLOTS to creates and saves the plots.

## customPlots

Module to create custom plots for the plotting module

Use this module like this:

```python
# Imports
from speechtotext.functions import BaseResult
from speechtotext.plot.plotting import Plotting

# Create class with matplotlib picture
class BoxPlotOfModelsWer(BasePlot):

        def create_plot(self) -> matplotlib.figure.Figure:
                plot = sns.boxplot(data=self.df, x="wer", y="model_name")
                fig = plot.get_figure()
                return fig

        def save_plot(self):
                fig = self.create_plot()
                fig.savefig(self.save_file_name)
# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(BoxPlotOfModelsWer)

# Create class with plotly picture
from speechtotext.plot.plotting import BasePlot, Plotting
class DemoPlotlyExample(BasePlot):

        def create_plot(self) -> plotly.graph_objs._figure.Figure:
                self.df = px.data.gapminder().query("country=='Canada'")
                fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
                return fig

# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(DemoPlotlyExample)
```


### _class_ speechtotext.plot.customPlots.CerByModelnameByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



### _class_ speechtotext.plot.customPlots.DurationByModelnameByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



### _class_ speechtotext.plot.customPlots.DurationLogByModelnameByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



### _class_ speechtotext.plot.customPlots.MeanOfMetricByModelname(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



### _class_ speechtotext.plot.customPlots.MerByModelnameByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



### _class_ speechtotext.plot.customPlots.WerByModelnameByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



### _class_ speechtotext.plot.customPlots.WilByModelnameByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



### _class_ speechtotext.plot.customPlots.WipByModelnameByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure
