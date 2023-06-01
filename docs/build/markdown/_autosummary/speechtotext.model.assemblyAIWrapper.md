# speechtotext.model.assemblyAIWrapper

Modelwrapper implemented for assemblyAi API.

ASSEMBLY_AI_API_KEY needs to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.assemblyAiWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
assemblyAiWrapper = assemblyAiAPIVersion(assemblyAiAPIVersion.assemblyAi_DEFAULT)

# Get model
assemblyAiWrapper.get_model()

# Benchmark choisen sample
assemblyAiWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = assemblyAiWrapper.benchmark_n_samples(dataset, number_of_samples)
```

### Classes

| [`AssemblyAIAPIVersion`](speechtotext.model.assemblyAIWrapper.AssemblyAIAPIVersion.md#speechtotext.model.assemblyAIWrapper.AssemblyAIAPIVersion)

 | Enum for the available assemblyAi API models.

 |
| [`AssemblyAIAPIWrapper`](speechtotext.model.assemblyAIWrapper.AssemblyAIAPIWrapper.md#speechtotext.model.assemblyAIWrapper.AssemblyAIAPIWrapper)

                    | Wrapper for assemblyAi API.

                                                                    |
