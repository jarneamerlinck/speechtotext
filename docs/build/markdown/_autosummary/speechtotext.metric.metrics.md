# speechtotext.metric.metrics

Module that calculates the metrics for speechtotext models.

Use this module like this:

```python
# Imports
from speechtotext.metric.metrics import Metrics

# Create metrics
m = Metrics("This is the original text, the source.", "This is the hypothesis text..", "id_from_dataset", duration=0.5)
print(m)
```

### Classes

| [`Metrics`](speechtotext.metric.metrics.Metrics.md#speechtotext.metric.metrics.Metrics)

 | Class to calulate the metrics.

 |
