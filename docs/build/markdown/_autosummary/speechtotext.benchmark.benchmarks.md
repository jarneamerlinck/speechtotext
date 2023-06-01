# speechtotext.benchmark.benchmarks

Module for benchmarks of speechtotext.

Use this module like this:

```python
# Imports
from speechtotext.datasets import Dataset
from speechtotext.benchmark.benchmarks import *

# Settings
number_of_samples = 10
report_name = "report name"
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
Benchmark.set_dataset(dataset)

# Create benchmark
wb = WhisperBenchmark()

# Run benchmark
wb(number_of_samples)

# Convert metrics to pandas dataframe
df = wb.convert_to_pandas()
print(df)

# Save metrics to csv (saves with datetime in name)
benchmark_results_to_csv([wb])

# Run benchmarks
## Settings
number_of_samples = 5
benchmark_dataset = dataset_RDH
benchmark_class_list: list[Benchmark] = [WhisperBenchmark, WhisperAPIBenchmark]

# Run benchmarks
results = run_benchmarks(benchmark_class_list, benchmark_dataset, number_of_samples, report_name)
```

### Functions

| [`run_benchmarks`](speechtotext.benchmark.benchmarks.run_benchmarks.md#speechtotext.benchmark.benchmarks.run_benchmarks)

 | Run al benchmarks out of list.

 |
### Classes

| [`Benchmark`](speechtotext.benchmark.benchmarks.Benchmark.md#speechtotext.benchmark.benchmarks.Benchmark)

                               | Benchmark is used to test/validate an model.

                |
