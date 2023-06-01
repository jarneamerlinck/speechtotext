# speechtotext.datasets.DatasetBare


### _class_ DatasetBare(path_to_dir, name, file_ext='.wav')
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Bare dataset class.

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

| `get_path_of_fragment`

 | Gets path of fragment.

 |
| `get_text_of_id`

                          | Get text of fragment id.

                                    |
| `number_of_samples`

                       | Get number of samples in dataset.

                           |
| `validate_samples`

                        | Validate if samples have a corresponding file.

              |

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
