# speechtotext.metric.customMetrics

Module to create custom metrics to save with the plots from the plotting module.

Use this module like this:

```python
# Imports
from speechtotext.functions import BaseResult
from speechtotext.plot.plotting import Plotting

# Create class with matplotlib picture
class BenchmarkResults(BaseMetrics):
        def create_df(self) -> pd.core.frame.DataFrame:
                return self.df

# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(BenchmarkResults)
```

### Classes

| [`BaseMetrics`](speechtotext.metric.customMetrics.BaseMetrics.md#speechtotext.metric.customMetrics.BaseMetrics)

 | Base class used to create metrics for result dataframe.

 |
| [`BenchmarkResults`](speechtotext.metric.customMetrics.BenchmarkResults.md#speechtotext.metric.customMetrics.BenchmarkResults)

                        | This class saves the results of the benchmark.

                                   |
| [`ErrorMetrics`](speechtotext.metric.customMetrics.ErrorMetrics.md#speechtotext.metric.customMetrics.ErrorMetrics)

                            | This class calulates the error statistic on the benchmark results.

               |
| [`ResultMetrics`](speechtotext.metric.customMetrics.ResultMetrics.md#speechtotext.metric.customMetrics.ResultMetrics)

                           | This class calulates the default statistic metrics on the benchmark results.

     |
