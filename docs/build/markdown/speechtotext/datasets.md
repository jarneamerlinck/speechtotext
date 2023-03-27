# Datasets

## speechtotext.datasets module


### _class_ speechtotext.datasets.Dataset(dir: str, file_ext: str = '.wav')
Bases: `object`


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



#### load_transcript()
Loads transcript
