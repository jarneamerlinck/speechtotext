# speechtotext.datasets.Dataset


### _class_ Dataset(path_to_dir, name, file_ext='.wav')
Bases: [`DatasetBare`](speechtotext.datasets.DatasetBare.md#speechtotext.datasets.DatasetBare)

Class to extract data from the dataset folder.

Creates dataset object.
There needs to be an transcripts.txt directly in the dir.
:type path_to_dir: [`str`](https://docs.python.org/3/library/stdtypes.html#str)
:param path_to_dir: Path to dir ending with “/”.
:type path_to_dir: str
:type name: [`str`](https://docs.python.org/3/library/stdtypes.html#str)
:param name: Name of dataset.
:type name: str
:type file_ext: [`str`](https://docs.python.org/3/library/stdtypes.html#str)
:param file_ext: Extention of files.
:type file_ext: str

### Methods

| `get_n_samples`

 | Get n random samples.

 |
| `get_path_of_fragment`

                    | Gets path of fragment.

                                      |
| `get_text_of_id`

                          | Get text of fragment id.

                                    |
| `load_transcript`

                         | Loads transcript.

                                           |
| `number_of_samples`

                       | Get number of samples in dataset.

                           |
| `validate_samples`

                        | Validate if samples have a corresponding file.

              |

#### get_n_samples(number_of_samples)
Get n random samples.


* **Parameters**

    **number_of_samples** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Number of random samples.



* **Returns**

    Dataset with the samples.



* **Return type**

    [SampleDataset](speechtotext.datasets.SampleDataset.md#speechtotext.datasets.SampleDataset)



#### get_path_of_fragment(audio_id)
Gets path of fragment.


* **Parameters**

    **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Id of file.



* **Raises**

    [**FileNotFoundError**](https://docs.python.org/3/library/exceptions.html#FileNotFoundError) – If id doesn’t exist.



* **Returns**

    Path to fragment.



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### get_text_of_id(audio_id)
Get text of fragment id.


* **Parameters**

    **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Id of fragment.



* **Returns**

    String of spoken text.



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### load_transcript()
Loads transcript.


#### number_of_samples()
Get number of samples in dataset.


* **Returns**

    Number of samples in dataset.



* **Return type**

    [int](https://docs.python.org/3/library/functions.html#int)



#### validate_samples()
Validate if samples have a corresponding file.


* **Returns**

    True if all samples have a file.



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)
