# speechtotext.model.azureWrapper

Modelwrapper implemented for Azure STT API.

AZURE_SPEECH_KEY API and AZURE_SPEECH_REGION need to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.azureWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
azureWrapper = AzureAPIVersion(AzureAPIVersion.AZURE_DEFAULT)

# Get model
azureWrapper.get_model()

# Benchmark choisen sample
azureWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = azureWrapper.benchmark_n_samples(dataset, number_of_samples)
```

### Classes

| [`AzureAPIVersion`](speechtotext.model.azureWrapper.AzureAPIVersion.md#speechtotext.model.azureWrapper.AzureAPIVersion)

 | Enum for the available AZURE API models.

 |
| [`AzureAPIWrapper`](speechtotext.model.azureWrapper.AzureAPIWrapper.md#speechtotext.model.azureWrapper.AzureAPIWrapper)

                         | Wrapper for AZURE API.

                                                                         |
### Exceptions

| [`AzureCancellation`](speechtotext.model.azureWrapper.AzureCancellation.md#speechtotext.model.azureWrapper.AzureCancellation)(message)

              | Exception when Azure gives an cancelation message.

                                             |
| [`AzureNoMatch`](speechtotext.model.azureWrapper.AzureNoMatch.md#speechtotext.model.azureWrapper.AzureNoMatch)(message)

                   | Exception when Azure finds not match.

                                                          |
