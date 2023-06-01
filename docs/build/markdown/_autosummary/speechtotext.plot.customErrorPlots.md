# speechtotext.plot.customErrorPlots

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

### Classes

| [`ErrorCountByModel`](speechtotext.plot.customErrorPlots.ErrorCountByModel.md#speechtotext.plot.customErrorPlots.ErrorCountByModel)

 | Class that is used to create error plots for an benchmark.

 |
| [`ErrorCountByModelByDataset`](speechtotext.plot.customErrorPlots.ErrorCountByModelByDataset.md#speechtotext.plot.customErrorPlots.ErrorCountByModelByDataset)

              | Class that is used to create error plots for an benchmark.

                                     |
| [`ErrorCountHeatmap`](speechtotext.plot.customErrorPlots.ErrorCountHeatmap.md#speechtotext.plot.customErrorPlots.ErrorCountHeatmap)

                       | Class that is used to create error plots for an benchmark.

                                     |
