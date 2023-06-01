# speechtotext.functions.BaseResult


### _class_ BaseResult(df, report_folder, file_name)
Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)

Parent class for results.
Child class should be made and added to Plotting.CUSTOM_RESULTS, Plotting.CUSTOM_ERRORS, Plotting.CUSTOM_PLOTS or Plotting.CUSTOM_ERROR_PLOTS

Creates object of BaseResult. Child class should be added to Plotting.CUSTOM_RESULTS.


* **Parameters**

    
    * **df** (*pd.core.frame.DataFrame*) – Dataframe that needs to be plotted.


    * **report_folder** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Path to report folder.


    * **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Name of saved File.


### Methods

| `save`

 | Saves Result to report folder.

 |

#### _abstract_ save()
Saves Result to report folder.
