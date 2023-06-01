# speechtotext.plot.plotting

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

### Classes

| [`BaseMatPlotLib`](speechtotext.plot.plotting.BaseMatPlotLib.md#speechtotext.plot.plotting.BaseMatPlotLib)

 | Parent class for custom plots with matplotlib.

 |
| [`BasePlotly`](speechtotext.plot.plotting.BasePlotly.md#speechtotext.plot.plotting.BasePlotly)

                              | Parent class for custom plots with Plotly.

                                                     |
| [`DynamicPlotClassesByMetricByDataset`](speechtotext.plot.plotting.DynamicPlotClassesByMetricByDataset.md#speechtotext.plot.plotting.DynamicPlotClassesByMetricByDataset)

     | Dynamically create plot classes for each metric for each database in the given dataframe.

      |
| [`DynamicPlotClassesByMetricForEachDataset`](speechtotext.plot.plotting.DynamicPlotClassesByMetricForEachDataset.md#speechtotext.plot.plotting.DynamicPlotClassesByMetricForEachDataset)

 | Dynamically create plot classes for each metric for each dataset in the given dataframe.

       |
| [`Plotting`](speechtotext.plot.plotting.Plotting.md#speechtotext.plot.plotting.Plotting)

                                 | Class that is used to create plots for an benchmark.

                                           |
