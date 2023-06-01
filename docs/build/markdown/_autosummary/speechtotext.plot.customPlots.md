# speechtotext.plot.customPlots

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

### Classes

| [`DynamicallyByModelNameByDataset`](speechtotext.plot.customPlots.DynamicallyByModelNameByDataset.md#speechtotext.plot.customPlots.DynamicallyByModelNameByDataset)

 | Class that is used to create plots for an benchmark.

 |
| [`DynamicallyByModelNameForEachDataset`](speechtotext.plot.customPlots.DynamicallyByModelNameForEachDataset.md#speechtotext.plot.customPlots.DynamicallyByModelNameForEachDataset)

    | Class that is used to create plots for an benchmark.

                                           |
| [`MetricHeatMap`](speechtotext.plot.customPlots.MetricHeatMap.md#speechtotext.plot.customPlots.MetricHeatMap)

                           | Class that is used to create plots for an benchmark.

                                           |
