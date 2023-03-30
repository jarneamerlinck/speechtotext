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



### speechtotext.functions.benchmark_results_to_csv(results: list[pandas.core.frame.DataFrame], save_name: str = 'reports/Benchmark_results_2023_03_30_H_47_38.csv')
Creates csv from benchmark results.


* **Parameters**

    
    * **results** (*list**[**pd.core.frame.DataFrame**]*) – List of results from benchmarks.


    * **save_name** (*str**, **optional*) – filename of output. Defaults to DEFAULT_CSV_NAME.



### speechtotext.functions.force_cudnn_initialization()
Force torch use for cuda.


### speechtotext.functions.join_benchmark_results(results: list[pandas.core.frame.DataFrame], set_index=True)
Join Benchmark results.


* **Parameters**

    
    * **results** (*list**[**pd.core.frame.DataFrame**]*) – results of benchmarks.


    * **set_index** (*bool**, **optional*) – Set True if [“model_name”, “audio_ID”] can be set as index. Defaults to True.



* **Returns**

    Dataframe with results of all benchmarks.



* **Return type**

    pd.core.frame.DataFrame



### speechtotext.functions.multidispatch(\*types)
Allow for Method overloading for classes.


### speechtotext.functions.save_folder_name(report_name: str, folder_name: str = 'reports')
Makes folder path


* **Parameters**

    
    * **report_name** (*str*) – name of report


    * **folder_name** (*str**, **optional*) – Name of folder. Defaults to DEFAULT_REPORT_FOLDER.



* **Returns**

    path to save folder



* **Return type**

    str



### speechtotext.functions.separate_benchmark_results_by_model(dataframe: DataFrame)
Seperate benchmark results for each model.


* **Parameters**

    **pd.core.frame.DataFrame** (*dataframe*) – Dataframe with results of all benchmarks.



* **Returns**

    results of benchmarks.



* **Return type**

    (list[pd.core.frame.DataFrame])



### speechtotext.functions.string_cleaning(text: str)
Cleaning of string for STT.


* **Parameters**

    **text** (*str*) – uncleaned string.



* **Returns**

    cleaned string.



* **Return type**

    str
