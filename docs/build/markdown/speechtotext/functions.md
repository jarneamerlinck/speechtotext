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



### _class_ speechtotext.functions.BaseResult(df: DataFrame, report_folder: str, file_name: str)
Bases: `ABC`


#### _abstract_ save()
Saves Result to report folder.


### _exception_ speechtotext.functions.RequiredEnvVariablesMissing(env_name: str)
Bases: `Exception`

Exception when an required env variable is missing.


### speechtotext.functions.benchmark_results_to_csv(results: list[pandas.core.frame.DataFrame], save_name: str = 'reports/Benchmark_results_2023_04_04_06_26_20.csv')
Creates csv from benchmark results.


* **Parameters**

    
    * **results** (*list**[**pd.core.frame.DataFrame**]*) – List of results from benchmarks.


    * **save_name** (*str**, **optional*) – filename of output. Defaults to DEFAULT_CSV_NAME.



### speechtotext.functions.force_cudnn_initialization()
Force torch use for cuda.


### speechtotext.functions.get_extention_of_file_name(file_name: str)
Get extention ofo file name.


* **Parameters**

    **file_name** (*str*) – File name



* **Returns**

    Extention of tile name



* **Return type**

    str



### speechtotext.functions.get_file_name_without_extention(file_name: str)
Get extention ofo file name.


* **Parameters**

    **file_name** (*str*) – File name



* **Returns**

    Extention of tile name



* **Return type**

    str



### speechtotext.functions.join_benchmark_results(results: list[pandas.core.frame.DataFrame], set_index=True)
Join Benchmark results.


* **Parameters**

    
    * **results** (*list**[**pd.core.frame.DataFrame**]*) – results of benchmarks.


    * **set_index** (*bool**, **optional*) – Set True if [“model_name”, “audio_ID”] can be set as index. Defaults to True.



* **Returns**

    Dataframe with results of all benchmarks.



* **Return type**

    pd.core.frame.DataFrame



### speechtotext.functions.load_env_variable(env_name: str)
Loads and returns env variable.


* **Parameters**

    **env_name** (*str*) – .env key



* **Raises**

    **RequiredEnvVariablesMissing** – Prints the variable name if its missing.



* **Returns**

    value of the .env key.



* **Return type**

    str



### speechtotext.functions.multidispatch(\*types)
Allow for Method overloading for classes.


### speechtotext.functions.save_folder_name(report_name: str, folder_name: str = 'reports')
Makes folder path.


* **Parameters**

    
    * **report_name** (*str*) – name of report.


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
