# speechtotext.functions

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

### Module attributes

| [`REGEX_STRING_PARSE`](speechtotext.functions.REGEX_STRING_PARSE.md#speechtotext.functions.REGEX_STRING_PARSE)
 | Regex used to clean the transcripts.

 |
| [`DEFAULT_DATETIME_FORMAT`](speechtotext.functions.DEFAULT_DATETIME_FORMAT.md#speechtotext.functions.DEFAULT_DATETIME_FORMAT)
                 | Default datetime format.

                                    |
| [`DEFAULT_REPORTS_FOLDER`](speechtotext.functions.DEFAULT_REPORTS_FOLDER.md#speechtotext.functions.DEFAULT_REPORTS_FOLDER)
                  | Default folder to save the reports.

                         |
| [`DEFAULT_CSV_NAME`](speechtotext.functions.DEFAULT_CSV_NAME.md#speechtotext.functions.DEFAULT_CSV_NAME)
                        | Default path to save Benchmark results.

                     |
### Functions

| [`benchmark_results_to_csv`](speechtotext.functions.benchmark_results_to_csv.md#speechtotext.functions.benchmark_results_to_csv)

                | Creates csv from benchmark results.

                         |
| [`force_cudnn_initialization`](speechtotext.functions.force_cudnn_initialization.md#speechtotext.functions.force_cudnn_initialization)

              | Force torch use for cuda if available.

                      |
| [`get_extention_of_file_name`](speechtotext.functions.get_extention_of_file_name.md#speechtotext.functions.get_extention_of_file_name)

              | Get extention of file name.

                                 |
| [`get_file_name_without_extention`](speechtotext.functions.get_file_name_without_extention.md#speechtotext.functions.get_file_name_without_extention)

         | Get extention of file name.

                                 |
| [`join_benchmark_results`](speechtotext.functions.join_benchmark_results.md#speechtotext.functions.join_benchmark_results)

                  | Join Benchmark results.

                                     |
| [`load_env_variable`](speechtotext.functions.load_env_variable.md#speechtotext.functions.load_env_variable)

                       | Loads and returns env variable.

                             |
| [`multidispatch`](speechtotext.functions.multidispatch.md#speechtotext.functions.multidispatch)

                           | Allow for Method overloading for classes.

                   |
| [`save_folder_name`](speechtotext.functions.save_folder_name.md#speechtotext.functions.save_folder_name)

                        | Makes folder path.

                                          |
| [`save_sub_folder_name`](speechtotext.functions.save_sub_folder_name.md#speechtotext.functions.save_sub_folder_name)

                    | Creates subfolder path.

                                     |
| [`separate_benchmark_results_by_model`](speechtotext.functions.separate_benchmark_results_by_model.md#speechtotext.functions.separate_benchmark_results_by_model)

     | Seperate benchmark results for each model.

                  |
| [`string_cleaning`](speechtotext.functions.string_cleaning.md#speechtotext.functions.string_cleaning)

                         | Cleaning of string for STT.

                                 |
| [`timing`](speechtotext.functions.timing.md#speechtotext.functions.timing)

                                  | Functions used to time duration of function.

                |
| [`uppercase_for_first_character_in_string`](speechtotext.functions.uppercase_for_first_character_in_string.md#speechtotext.functions.uppercase_for_first_character_in_string)

 | Return string where first character is uppercase.

           |
### Classes

| [`BaseResult`](speechtotext.functions.BaseResult.md#speechtotext.functions.BaseResult)

                              | Parent class for results.

                                   |
### Exceptions

| [`NoTranscriptReturned`](speechtotext.functions.NoTranscriptReturned.md#speechtotext.functions.NoTranscriptReturned)()

                  | Exception when API does not return a transcript.

            |
| [`RequiredEnvVariablesMissing`](speechtotext.functions.RequiredEnvVariablesMissing.md#speechtotext.functions.RequiredEnvVariablesMissing)(env_name)

   | Exception when an required env variable is missing.

         |
