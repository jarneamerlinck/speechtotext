# Code Examples for speechtotext

This page is an collection of examples of how to use the package.

## Full usage example

**NOTE**: The `.env` file might have to be loaded before running the benchmarks.

```python
from dotenv import load_dotenv
load_dotenv()
```

Use this module like this:

```python
# Imports
import speechtotext
from speechtotext.datasets import Dataset
from speechtotext.benchmark.customBenchmarks import *
from speechtotext.benchmark.benchmarks import run_benchmarks, Benchmark
from speechtotext.functions import force_cudnn_initialization
from speechtotext.plot.plotting import Plotting

import speechtotext.metric.customMetrics
force_cudnn_initialization()

# Load dataset
dataset = Dataset(path_to_dir="path/to/dataset", name= "dataset_name")

# Settings to run benchmarks
number_of_samples = 100
report_name = "benchmark_name"

benchmark_class_list: list[Benchmark] = [WhisperBenchmark, WhisperAPIBenchmark]

# Run benchmarks
results = run_benchmarks(benchmark_class_list, dataset, number_of_samples, report_name)

# Create plots
plotting = Plotting(results=results, errors=Benchmark.ERROR_LIST, report_name = report_name)
plotting.save_all()
```

## Add new model wrapper and benchmark

To add an new model to benchmark the following classes need to be made:


* ModelWrapper


* ModelVersion


* Benchmark

### Create new ModelWrapper

```python
from speechtotext.model.modelWrapper import *
from speechtotext.functions import load_env_variable

# Model version
class CustomModelVersion(ModelVersion):
        MODEL_VERSION_1         = "version_1"
        MODEL_VERSION_2         = "version_2"
        MODEL_VERSION_ENHANCED  = "enhanced"

# Model wrapper
class CustomModelWrapper(ModelWrapper):

        LANGUAGE_CODE:str = 'nl'

        def __init__(self, model_version:CustomModelVersion):
                """Force correct model_version.
                """
                super().__init__(model_version)

        def get_model(self):
                """Load model or setup for API call.
                """
                self.API_KEY = load_env_variable("MODEL_API_KEY")
                self.model = model()

        def get_transcript_of_file(self, audio_file_name:str) -> str:
                """Get transcript of audio file."""
                result = self.model.transcribe(self.API_KEY, audio_file_name)
                return result["text"]
```

### Create new Benchmark

```python
from speechtotext.benchmark.benchmarks import *
from speechtotext.model.modelWrapper import ModelWrapper

class CustomModelBenchmark(Benchmark):
        MODEL_BASE = "Custom model name"

        def create_models(self) -> list[ModelWrapper]:
                models = []
                for version in CustomModelVersion:
                        models.append(CustomModelWrapper(version))
                return models
```

### Use custom benchmarks

```python
# Imports
import speechtotext
from speechtotext.datasets import Dataset
from speechtotext.benchmark.customBenchmarks import *
from speechtotext.benchmark.benchmarks import run_benchmarks, Benchmark
from speechtotext.functions import force_cudnn_initialization
from speechtotext.plot.plotting import Plotting

import speechtotext.metric.customMetrics
force_cudnn_initialization()

# Load dataset
dataset = Dataset(path_to_dir="path/to/dataset", name= "dataset_name")

# Settings to run benchmarks
number_of_samples = 100
report_name = "benchmark_name"

benchmark_class_list: list[Benchmark] = [WhisperBenchmark, WhisperAPIBenchmark, CustomModelBenchmark]

# Run benchmarks
results = run_benchmarks(benchmark_class_list, dataset, number_of_samples, report_name)

# Create plots
plotting = Plotting(results=results, errors=Benchmark.ERROR_LIST, report_name = report_name)
plotting.save_all()
```
