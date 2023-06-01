# speechtotext.datasets

Module to create the datasets for the speechtotext package.

The dataset requires an `transcripts.txt` in the dataset folder. In there are relative links to the audiofiles followed by `|` and the transcript of that file.

Example of entry:

```default
20000_mijlen/20000_mijlen_0001.wav|This is the trancsript of the audio
```

Use this module like this:

```python
# Imports
from speechtotext.datasets import Dataset
from speechtotext.benchmarks import *

# Settings
path_to_dir = "path/to/dir"
dataset_name = "dataset_name"
id = "existing_id"
number_of_samples = 10

# Create dataset
dataset = Dataset(path_to_dir=path_to_dir, name= dataset_name)

# Print number of samples
print(dataset.number_of_samples())

# Get audio file from id
dataset.get_path_of_fragment(id)

# Get transcript from id
dataset.get_text_of_id(id)

# Get n trandom samples
dataset_n_random: SampleDataset = dataset.get_n_samples(number_of_samples)
```

### Classes

| [`Dataset`](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset)

 | Class to extract data from the dataset folder.

 |
| [`DatasetBare`](speechtotext.datasets.DatasetBare.md#speechtotext.datasets.DatasetBare)

                             | Bare dataset class.

                                         |
| [`SampleDataset`](speechtotext.datasets.SampleDataset.md#speechtotext.datasets.SampleDataset)

                           | Sample of dataset.

                                          |
