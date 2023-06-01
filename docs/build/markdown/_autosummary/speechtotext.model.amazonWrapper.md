# speechtotext.model.amazonWrapper

Modelwrapper implemented for Amazon STT API.

AMAZON API. AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AMAZON_REGION and AMAZON_BUCKET  need to be in the ‘.env’.

Use this module like this:

```python
# Imports
from speechtotext.model.amazonWrapper import *
from speechtotext.benchmark.benchmarks import *
from speechtotext.datasets import Dataset

# Create dataset
number_of_samples = 10
dataset = Dataset(path_to_dir="path/to/dir", name= "dataset_name")
id = "existing_audio_id"
number_of_samples = 10

# Create wrapper
amazonWrapper = AmazonAPIVersion(AmazonAPIVersion.AMAZON_DEFAULT)

# Get model
amazonWrapper.get_model()

# Benchmark choisen sample
amazonWrapper.benchmark_sample(dataset, id)

# Benchmark n random samples
array = amazonWrapper.benchmark_n_samples(dataset, number_of_samples)
```

### Functions

| [`amazon_delete_job`](speechtotext.model.amazonWrapper.amazon_delete_job.md#speechtotext.model.amazonWrapper.amazon_delete_job)

 | Deletes a transcription job.

 |
### Classes

| [`AmazonAPIVersion`](speechtotext.model.amazonWrapper.AmazonAPIVersion.md#speechtotext.model.amazonWrapper.AmazonAPIVersion)

                        | Enum for the available AMAZON API models.

                                                  |
| [`AmazonAPIWrapper`](speechtotext.model.amazonWrapper.AmazonAPIWrapper.md#speechtotext.model.amazonWrapper.AmazonAPIWrapper)

                        | Wrapper for AMAZON API.

                                                                    |
