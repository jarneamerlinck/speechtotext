# speechtotext.model.deepgramWrapper

Modelwrapper implemented for deepgram API.

DEEPGRAM_API_KEY needs to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.deepgramWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
deepgramWrapper = deepgramAPIVersion(deepgramAPIVersion.deepgram_DEFAULT)

# Get model
deepgramWrapper.get_model()

# Benchmark choisen sample
deepgramWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = deepgramWrapper.benchmark_n_samples(dataset, number_of_samples)
```

### Classes

| [`DeepgramAPIVersion`](speechtotext.model.deepgramWrapper.DeepgramAPIVersion.md#speechtotext.model.deepgramWrapper.DeepgramAPIVersion)

 | Enum for the available deepgram API models.

 |
| [`DeepgramAPIWrapper`](speechtotext.model.deepgramWrapper.DeepgramAPIWrapper.md#speechtotext.model.deepgramWrapper.DeepgramAPIWrapper)

                      | Wrapper for deepgram API.

                                                                      |
