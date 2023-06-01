# speechtotext.model.speechmaticsWrapper

Modelwrapper implemented for Speechmatics STT API.

**WARNING**: Package version speechmatics-python==1.6.4 is needed to run the script. Errors on 1.7.0

SPEECHMATICS_API_KEY needs to be in the ‘.env’ file in current directory.

Use this module like this:

```python
# Imports
from speechtotext.model.speechmaticsWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
speechmaticsWrapper = SpeechmaticsAPIVersion(SpeechmaticsAPIVersion.SPEECHMATICS_DEFAULT)

# Get model
speechmaticsWrapper.get_model()

# Benchmark choisen sample
speechmaticsWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = speechmaticsWrapper.benchmark_n_samples(dataset, number_of_samples)
```

### Classes

| [`SpeechmaticsAPIVersion`](speechtotext.model.speechmaticsWrapper.SpeechmaticsAPIVersion.md#speechtotext.model.speechmaticsWrapper.SpeechmaticsAPIVersion)

 | Enum for the available SPEECHMATICS API models.

 |
| [`SpeechmaticsAPIWrapper`](speechtotext.model.speechmaticsWrapper.SpeechmaticsAPIWrapper.md#speechtotext.model.speechmaticsWrapper.SpeechmaticsAPIWrapper)

                  | Wrapper for SPEECHMATICS API.

                                                                  |
