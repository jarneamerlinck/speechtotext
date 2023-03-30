# Datasets

## speechtotext.datasets module

Module to create the datasets for the speechtotext package.

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


### _class_ speechtotext.datasets.Dataset(path_to_dir: str, name: str, file_ext: str = '.wav')
Bases: `DatasetBare`

Class to extract data from the dataset folder.


#### get_n_samples(number_of_samples: int)
Get n random samples.


* **Parameters**

    **number_of_samples** (*int*) – Number of random samples.



* **Returns**

    dataset with the samples.



* **Return type**

    SampleDataset



#### load_transcript()
Loads transcript.


### _class_ speechtotext.datasets.DatasetBare(path_to_dir: str, name: str, file_ext: str = '.wav')
Bases: `object`

Bare dataset class.


#### get_path_of_fragment(id: str)
Gets path of fragment.


* **Parameters**

    **id** (*str*) – id of file.



* **Raises**

    **FileNotFoundError** – if id doesn’t exist.



* **Returns**

    Path to fragment.



* **Return type**

    str



#### get_text_of_id(id: str)
Get text of fragment id.


* **Parameters**

    **id** (*str*) – id of fragment.



* **Returns**

    string of spoken text.



* **Return type**

    str



#### number_of_samples()
Get number of samples in dataset.


* **Returns**

    Number of samples in dataset.



* **Return type**

    int



### _class_ speechtotext.datasets.SampleDataset(df: DataFrame, path_to_dir: str, name: str, file_ext: str = '.wav')
Bases: `DatasetBare`

Sample of dataset.
