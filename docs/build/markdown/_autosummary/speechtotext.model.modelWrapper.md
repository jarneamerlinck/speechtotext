# speechtotext.model.modelWrapper

Module with the parent classes for the model wrapper. Needs to be implemented to use the benchmarks.

Use this module like this:

```python
# Imports
from speechtotext.model.moduleWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create child class for ModelVersion
class ChildModelVersion(ModelVersion):
        MODEL_VERSION   = "demo"

# Create child class for ModelWrapper
class ChildModelWrapper(ModelWrapper):
        def __init__(self, model_version:ChildModelVersion):

                self.model_version = model_version

        def get_model(self, model:modelType):
                self.model = model

        def get_transcript_of_file(self, audio_file_name:str) -> str:
                result = self.model.transcribe(audio_file_name)
                return result["text"]

# Create child class of benchmark
class ChildBenchmark(Benchmark):
        MODEL_BASE = "model_name"

        def create_models(self) -> list[ModelWrapper]:
                models = []
                for version in ChildModelVersion:
                        models.append(ChildModelWrapper(version))
                return models

# Create benchmark
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
Benchmark.set_dataset(dataset)

benchmark = ChildBenchmark()

# Run benchmark
benchmark(number_of_samples)
```

### Classes

| [`MetaModelWrapper`](speechtotext.model.modelWrapper.MetaModelWrapper.md#speechtotext.model.modelWrapper.MetaModelWrapper)

 | Meta class for model wrapper.

 |
| [`ModelVersion`](speechtotext.model.modelWrapper.ModelVersion.md#speechtotext.model.modelWrapper.ModelVersion)

                            | Enum for the Available models.

                                                                 |
| [`ModelWrapper`](speechtotext.model.modelWrapper.ModelWrapper.md#speechtotext.model.modelWrapper.ModelWrapper)

                            | Abstract Wrapper for model.

                                                                    |
