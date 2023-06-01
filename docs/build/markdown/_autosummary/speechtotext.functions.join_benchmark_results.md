# speechtotext.functions.join_benchmark_results


### join_benchmark_results(results, set_index=True)
Join Benchmark results.


* **Parameters**

    
    * **results** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[**pd.core.frame.DataFrame**]*) – Results of benchmarks.


    * **set_index** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Set True if [“model_name”, “audio_ID”] can be set as index. Defaults to True.



* **Returns**

    Dataframe with results of all benchmarks.



* **Return type**

    pd.core.frame.DataFrame
