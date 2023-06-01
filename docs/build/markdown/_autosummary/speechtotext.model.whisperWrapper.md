# speechtotext.model.whisperWrapper

Modelwrapper implemented for whisper. Local and API.

API OPENAI_API_KEY and OPENAI_ORGANIZATION need to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.whisperWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
whisperWrapper = WhisperWrapper(WhisperVersion.TINY)
# Add model to Plotting
# Get model
whisperWrapper.get_model()

# Benchmark choisen sample
whisperWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = whisperWrapper.benchmark_n_samples(dataset, number_of_samples)
```

### Classes

| [`WhisperAPIVersion`](speechtotext.model.whisperWrapper.WhisperAPIVersion.md#speechtotext.model.whisperWrapper.WhisperAPIVersion)

 | Enum for the available Whisper API models.

 |
| [`WhisperAPIWrapper`](speechtotext.model.whisperWrapper.WhisperAPIWrapper.md#speechtotext.model.whisperWrapper.WhisperAPIWrapper)

                       | Wrapper for whisper API.

                                                                       |
| [`WhisperVersion`](speechtotext.model.whisperWrapper.WhisperVersion.md#speechtotext.model.whisperWrapper.WhisperVersion)

                          | Enum for the available Whisper models.

                                                         |
| [`WhisperWrapper`](speechtotext.model.whisperWrapper.WhisperWrapper.md#speechtotext.model.whisperWrapper.WhisperWrapper)

                          | Wrapper for whisper model.

                                                                     |
