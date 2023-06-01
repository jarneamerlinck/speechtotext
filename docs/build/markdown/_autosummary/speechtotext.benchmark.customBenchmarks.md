# speechtotext.benchmark.customBenchmarks

Module for benchmarks of speechtotext.

Use this module like this:

```python
# Imports
from speechtotext.datasets import Dataset
from speechtotext.benchmark.benchmarks import *

# Settings
number_of_samples = 10
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
```

### Classes

| [`AmazonAPIBenchmark`](speechtotext.benchmark.customBenchmarks.AmazonAPIBenchmark.md#speechtotext.benchmark.customBenchmarks.AmazonAPIBenchmark)

 | Benchmark for Amazon API transcribe.

 |
| [`AssemblyAIAPIBenchmark`](speechtotext.benchmark.customBenchmarks.AssemblyAIAPIBenchmark.md#speechtotext.benchmark.customBenchmarks.AssemblyAIAPIBenchmark)

                  | Benchmark for AssemblyAI API.

                               |
| [`AzureAPIBenchmark`](speechtotext.benchmark.customBenchmarks.AzureAPIBenchmark.md#speechtotext.benchmark.customBenchmarks.AzureAPIBenchmark)

                       | Benchmark for Azure API.

                                    |
| [`DeepgramAPIBenchmark`](speechtotext.benchmark.customBenchmarks.DeepgramAPIBenchmark.md#speechtotext.benchmark.customBenchmarks.DeepgramAPIBenchmark)

                    | Benchmark for Deepgram API.

                                 |
| [`GoogleAPIBenchmark`](speechtotext.benchmark.customBenchmarks.GoogleAPIBenchmark.md#speechtotext.benchmark.customBenchmarks.GoogleAPIBenchmark)

                      | Benchmark for Google API transcribe.

                        |
| [`SpeechmaticsAPIBenchmark`](speechtotext.benchmark.customBenchmarks.SpeechmaticsAPIBenchmark.md#speechtotext.benchmark.customBenchmarks.SpeechmaticsAPIBenchmark)

                | Benchmark for Speechmatics API.

                             |
| [`WhisperAPIBenchmark`](speechtotext.benchmark.customBenchmarks.WhisperAPIBenchmark.md#speechtotext.benchmark.customBenchmarks.WhisperAPIBenchmark)

                     | Benchmark for API whisper models.

                           |
| [`WhisperBenchmark`](speechtotext.benchmark.customBenchmarks.WhisperBenchmark.md#speechtotext.benchmark.customBenchmarks.WhisperBenchmark)

                        | Benchmark for local whisper models.

                         |
