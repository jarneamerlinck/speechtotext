# speechtotext plot package

## plotting

Module that plots the results from the benchmarks.

Use this module like this:

```python
# Imports
from speechtotext.plot.plotting import BasePlot, Plotting

# Create plotting object
plotting = Plotting(results=results, errors=errors, report_name="report_name")

# Create all custom plots that are added to Plotting.CUSTOM_RESULTS, Plotting.CUSTOM_ERRORS, Plotting.CUSTOM_PLOTS, Plotting.CUSTOM_ERROR_PLOTS
# The Plotting.CUSTOM_ERROR_PLOTS and Plotting.CUSTOM_ERRORS will be saved in the `error_plots` directory.
plotting.save_all()
```


### _class_ speechtotext.plot.plotting.BaseMatPlotLib(df: DataFrame, report_folder: str, file_name: str)
Bases: [`BaseResult`](../index.md#speechtotext.functions.BaseResult)

Parent class for custom plots with matplotlib. Code can be generated from d-tale.
Child class should be made and added to Plotting.CUSTOM_RESULTS, Plotting.CUSTOM_ERRORS, Plotting.CUSTOM_PLOTS or Plotting.CUSTOM_ERROR_PLOTS


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

Parent class for custom plots with Plotly. Code can be generated from d-tale.
Child class should be made and added to Plotting.CUSTOM_RESULTS, Plotting.CUSTOM_ERRORS, Plotting.CUSTOM_PLOTS or Plotting.CUSTOM_ERROR_PLOTS


#### _abstract_ create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



#### save()
Saves plot to folder.


### _class_ speechtotext.plot.plotting.DynamicPlotClassesByMetricByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: [`BaseResult`](../index.md#speechtotext.functions.BaseResult)

Dynamically create plot classes for each metric for each database in the given dataframe. This class is a parent class. The child class should be added to Plotting.CUSTOM_PLOTS.


#### _abstract_ create_plot()

#### create_plot_classes()
Creates plot classes.


#### save()
Saves plot to folder.


### _class_ speechtotext.plot.plotting.DynamicPlotClassesByMetricForEachDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: [`BaseResult`](../index.md#speechtotext.functions.BaseResult)

Dynamically create plot classes for each metric for each dataset in the given dataframe. This class is a parent class. The child class should be added to Plotting.CUSTOM_PLOTS.


#### _abstract_ create_plot()

#### create_plot_classes()
Creates plot classes.


#### save()
Saves plot to folder.


### _class_ speechtotext.plot.plotting.Plotting(results: list[pandas.core.frame.DataFrame], errors: list[pandas.core.frame.DataFrame], report_name: str)
Bases: `object`

Class that is used to create plots for an benchmark.


#### CUSTOM_ERRORS(_: list[[speechtotext.functions.BaseResult](../index.md#speechtotext.functions.BaseResult)_ _ = [_ )
List of error classes that need to be saved.

This could be an pandas df, report text file, …


* **Type**

    list[[BaseResult](../index.md#speechtotext.functions.BaseResult)]



#### CUSTOM_ERROR_PLOTS(_: list[[speechtotext.functions.BaseResult](../index.md#speechtotext.functions.BaseResult)_ _ = [_ )
List of error plot classes that need to be saved.

This could be an plotly, matplotlib or another plot.


* **Type**

    list[[BaseResult](../index.md#speechtotext.functions.BaseResult)]



#### CUSTOM_PLOTS(_: list[[speechtotext.functions.BaseResult](../index.md#speechtotext.functions.BaseResult)_ _ = [_ )
List of plot classes that need to be saved.

This could be an plotly, matplotlib or another plot.


* **Type**

    list[[BaseResult](../index.md#speechtotext.functions.BaseResult)]



#### CUSTOM_RESULTS(_: list[[speechtotext.functions.BaseResult](../index.md#speechtotext.functions.BaseResult)_ _ = [<class 'speechtotext.metric.customMetrics.BenchmarkResults'>, <class 'speechtotext.metric.customMetrics.ResultMetrics'>_ )
List of result classes that need to be saved.

This could be an pandas df, report text file, …


* **Type**

    list[[BaseResult](../index.md#speechtotext.functions.BaseResult)]



#### DATASET_NAMES(_: list[str_ _ = [_ )
List of dataset names that were used for the benchmarks.


* **Type**

    list[str]



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
Plotting.CUSTOM_PLOTS.append(BoxPlotOfModelsWer)

# Create class with plotly picture
from speechtotext.plot.plotting import BasePlot, Plotting
class DemoPlotlyExample(BasePlot):

        def create_plot(self) -> plotly.graph_objs._figure.Figure:
                self.df = px.data.gapminder().query("country=='Canada'")
                fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
                return fig

# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(DemoPlotlyExample)
```


### _class_ speechtotext.plot.customPlots.DynamicallyByModelNameByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `DynamicPlotClassesByMetricByDataset`

Class that is used to create plots for an benchmark.


#### create_plot()

### _class_ speechtotext.plot.customPlots.DynamicallyByModelNameForEachDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `DynamicPlotClassesByMetricForEachDataset`

Class that is used to create plots for an benchmark.


#### create_plot()
## customErrorPlots

Module to create custom error plots for the plotting module

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
Plotting.CUSTOM_ERRORS.append(BoxPlotOfModelsWer)

# Create class with plotly picture
from speechtotext.plot.plotting import BasePlot, Plotting
class DemoPlotlyExample(BasePlot):

        def create_plot(self) -> plotly.graph_objs._figure.Figure:
                self.df = px.data.gapminder().query("country=='Canada'")
                fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
                return fig

# Add model to Plotting
Plotting.CUSTOM_ERRORS.append(DemoPlotlyExample)
```


### _class_ speechtotext.plot.customErrorPlots.ErrorCountByModel(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create error plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



### _class_ speechtotext.plot.customErrorPlots.ErrorCountByModelByDataset(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create error plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure



### _class_ speechtotext.plot.customErrorPlots.ErrorCountHeatmap(df: DataFrame, report_folder: str, file_name: str)
Bases: `BasePlotly`

Class that is used to create error plots for an benchmark.


#### create_plot()
Creates plot to be saved.


* **Returns**

    Plot that needs to be saved.



* **Return type**

    plotly.graph_objs._figure.Figure
