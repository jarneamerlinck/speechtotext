# Functions

## speechtotext.functions module

Module with functions for the speechtotext package.

Use this module like this:

```python
# Imports
from speechtotext.functions import *

# Force torch use for cuda
force_cudnn_initialization()

# Clean string
string_cleaning("this has.//./8 to be cleaned::@")
```


### speechtotext.functions.REGEX_STRING_PARSE()
Regex string parce used to clean up transcripts that are used to validate the speechtotext models.


* **Type**

    str



### speechtotext.functions.force_cudnn_initialization()
Force torch use for cuda.


### speechtotext.functions.multidispatch(\*types)
Allow for Method overloading.


### speechtotext.functions.string_cleaning(text: str)
Cleaning of string for STT.


* **Parameters**

    **text** (*str*) – uncleaned string.



* **Returns**

    cleaned string.



* **Return type**

    str
