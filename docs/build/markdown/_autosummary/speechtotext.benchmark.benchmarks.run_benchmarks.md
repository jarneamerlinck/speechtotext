# speechtotext.benchmark.benchmarks.run_benchmarks


### run_benchmarks(benchmark_class_list, benchmark_dataset, number_of_samples, report_name)
Run al benchmarks out of list.


* **Parameters**

    
    * **benchmark_list** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Benchmark*](speechtotext.benchmark.benchmarks.Benchmark.md#speechtotext.benchmark.benchmarks.Benchmark)*]*) – List of benchmark classes to run.


    * **dataset** ([*Dataset*](speechtotext.datasets.Dataset.md#speechtotext.datasets.Dataset)) – Dataset to use for benchmark.


    * **number_of_samples** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Number of samples used in benchmark.


    * **report_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Name of report. To save the errors to.



* **Return type**

    [`list`](https://docs.python.org/3/library/stdtypes.html#list)[`DataFrame`]
