# Datasets

## speechtotext.datasets module


### _class_ speechtotext.datasets.Dataset(path_to_dir: str, name: str, file_ext: str = '.wav')
Bases: `DatasetBare`


#### get_n_samples(number_of_samples: int)
Get n random samples


* **Parameters**

    **number_of_samples** (*int*) – Number of random samples



* **Returns**

    dataset with the samples



* **Return type**

    SampleDataset



#### load_transcript()
Loads transcript


### _class_ speechtotext.datasets.DatasetBare(path_to_dir: str, name: str, file_ext: str = '.wav')
Bases: `object`

Bare dataset class


#### get_path_of_fragment(id: str)
Gets path of fragment


* **Parameters**

    **id** (*str*) – id of file



* **Raises**

    **FileNotFoundError** – if id doesn’t exist



* **Returns**

    _description_



* **Return type**

    str



#### get_text_of_id(id: str)
Get text of fragment id


* **Parameters**

    **id** (*str*) – id of fragment



* **Returns**

    string of spoken text



* **Return type**

    str



#### number_of_samples()
Get number of samples in dataset


* **Returns**

    Number of samples in dataset



* **Return type**

    int



### _class_ speechtotext.datasets.SampleDataset(df: DataFrame, path_to_dir: str, name: str, file_ext: str = '.wav')
Bases: `DatasetBare`
