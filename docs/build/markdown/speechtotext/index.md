# speechtotext package

This package is used to test and validate Speech2text models.

## functions

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


### _class_ speechtotext.functions.BaseResult(df: DataFrame, report_folder: str, file_name: str)
Bases: `ABC`

Parent class for results.
Child class should be made and added to Plotting.CUSTOM_RESULTS, Plotting.CUSTOM_ERRORS, Plotting.CUSTOM_PLOTS or Plotting.CUSTOM_ERROR_PLOTS


#### _abstract_ save()
Saves Result to report folder.


### speechtotext.functions.DEFAULT_CSV_NAME(_: st_ _ = 'reports/Benchmark_results_2023_05_02_12_55_36.csv_ )
Default path to save Benchmark results.


* **Type**

    str



### speechtotext.functions.DEFAULT_DATETIME_FORMAT(_: st_ _ = '2023_05_02_12_55_36_ )
Default datetime format. (Uses string format for datetime)


* **Type**

    str



### speechtotext.functions.DEFAULT_REPORTS_FOLDER(_: st_ _ = 'reports_ )
Default folder to save the reports.


* **Type**

    str



### speechtotext.functions.REGEX_STRING_PARSE(_: st_ _ = '[^A-Za-z0-9 ]+_ )
Regex used to clean the transcripts.


* **Type**

    str



### _exception_ speechtotext.functions.RequiredEnvVariablesMissing(env_name: str)
Bases: `Exception`

Exception when an required env variable is missing.


### speechtotext.functions.benchmark_results_to_csv(results: list[pandas.core.frame.DataFrame], save_name: str = 'reports/Benchmark_results_2023_05_02_12_55_36.csv')
Creates csv from benchmark results.


* **Parameters**

    
    * **results** (*list**[**pd.core.frame.DataFrame**]*) – List of results from benchmarks.


    * **save_name** (*str**, **optional*) – Filename of output. Defaults to DEFAULT_CSV_NAME.



### speechtotext.functions.force_cudnn_initialization()
Force torch use for cuda if available.


### speechtotext.functions.get_extention_of_file_name(file_name: str)
Get extention of file name.


* **Parameters**

    **file_name** (*str*) – File name.



* **Returns**

    Extention of tile name.



* **Return type**

    str



### speechtotext.functions.get_file_name_without_extention(file_name: str)
Get extention of file name.


* **Parameters**

    **file_name** (*str*) – File name.



* **Returns**

    Extention of tile name.



* **Return type**

    str



### speechtotext.functions.join_benchmark_results(results: list[pandas.core.frame.DataFrame], set_index=True)
Join Benchmark results.


* **Parameters**

    
    * **results** (*list**[**pd.core.frame.DataFrame**]*) – Results of benchmarks.


    * **set_index** (*bool**, **optional*) – Set True if [“model_name”, “audio_ID”] can be set as index. Defaults to True.



* **Returns**

    Dataframe with results of all benchmarks.



* **Return type**

    pd.core.frame.DataFrame



### speechtotext.functions.load_env_variable(env_name: str)
Loads and returns env variable.


* **Parameters**

    **env_name** (*str*) – .env key.



* **Raises**

    **RequiredEnvVariablesMissing** – Prints the variable name if its missing.



* **Returns**

    Value of the .env key.



* **Return type**

    str



### speechtotext.functions.multidispatch(\*types)
Allow for Method overloading for classes.


### speechtotext.functions.save_folder_name(report_name: str, folder_name: str = 'reports')
Makes folder path.


* **Parameters**

    
    * **report_name** (*str*) – Name of report.


    * **folder_name** (*str**, **optional*) – Name of folder. Defaults to DEFAULT_REPORT_FOLDER.



* **Returns**

    path to save folder.



* **Return type**

    str



### speechtotext.functions.save_sub_folder_name(folder_path: str, subfolder_name: str)
Creates subfolder path.


* **Parameters**

    
    * **folder_path** (*str*) – Path of parent folder.


    * **subfolder_name** (*str*) – Subfolder name.



* **Returns**

    Path to save folder.



* **Return type**

    str



### speechtotext.functions.separate_benchmark_results_by_model(dataframe: DataFrame)
Seperate benchmark results for each model.


* **Parameters**

    **pd.core.frame.DataFrame** (*dataframe*) – Dataframe with results of all benchmarks.



* **Returns**

    Results of benchmarks.



* **Return type**

    (list[pd.core.frame.DataFrame])



### speechtotext.functions.string_cleaning(text: str)
Cleaning of string for STT.


* **Parameters**

    **text** (*str*) – Uncleaned string.



* **Returns**

    Cleaned string.



* **Return type**

    str



### speechtotext.functions.timing(f)
Functions used to time duration of function.


### speechtotext.functions.uppercase_for_first_character_in_string(string: str)
Return string where first character is uppercase.


* **Parameters**

    **string** (*str*) – String to process.



* **Returns**

    String where first character is uppercase.



* **Return type**

    str


## datasets

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


### _class_ speechtotext.datasets.Dataset(path_to_dir: str, name: str, file_ext: str = '.wav')
Class to extract data from the dataset folder.


#### get_n_samples(number_of_samples: int)
Get n random samples.


* **Parameters**

    **number_of_samples** (*int*) – Number of random samples.



* **Returns**

    Dataset with the samples.



* **Return type**

    SampleDataset



#### load_transcript()
Loads transcript.


### _class_ speechtotext.datasets.DatasetBare(path_to_dir: str, name: str, file_ext: str = '.wav')
Bare dataset class.


#### get_path_of_fragment(id: str)
Gets path of fragment.


* **Parameters**

    **id** (*str*) – Id of file.



* **Raises**

    **FileNotFoundError** – If id doesn’t exist.



* **Returns**

    Path to fragment.



* **Return type**

    str



#### get_text_of_id(id: str)
Get text of fragment id.


* **Parameters**

    **id** (*str*) – Id of fragment.



* **Returns**

    String of spoken text.



* **Return type**

    str



#### number_of_samples()
Get number of samples in dataset.


* **Returns**

    Number of samples in dataset.



* **Return type**

    int



### _class_ speechtotext.datasets.SampleDataset(df: DataFrame, path_to_dir: str, name: str, file_ext: str = '.wav')
Sample of dataset.
