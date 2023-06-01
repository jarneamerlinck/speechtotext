# speechtotext.model.googleWrapper

Modelwrapper implemented for google STT API.

GOOGLE_APPLICATION_CREDENTIALS needs to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.googleWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
googleWrapper = googleAPIVersion(googleAPIVersion.google_DEFAULT)

# Get model
googleWrapper.get_model()

# Benchmark choisen sample
googleWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = googleWrapper.benchmark_n_samples(dataset, number_of_samples)
```

### Classes

| [`GoogleAPIVersion`](speechtotext.model.googleWrapper.GoogleAPIVersion.md#speechtotext.model.googleWrapper.GoogleAPIVersion)

 | Enum for the available google API models.

 |
| [`GoogleAPIWrapper`](speechtotext.model.googleWrapper.GoogleAPIWrapper.md#speechtotext.model.googleWrapper.GoogleAPIWrapper)

                        | Wrapper for google API.

                                                                        |
