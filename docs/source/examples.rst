Code Examples for speechtotext package
======================================

This page is an collection of examples of how to use the package.

Requirements
------------

* Folder with datasets and the ``transcripts.txt`` to test the models.

* Contents of ``.env`` in the directory of the python script.

	* For whisper

	.. code-block:: shell

		OPENAI_API_KEY=sk-somemorerandomnumberlettersandmorerandomnessform
		OPENAI_ORGANIZATION=org-somerandomnumberandlette

	* For Amazon

	.. code-block:: shell

		AWS_ACCESS_KEY_ID = access-id
		AWS_SECRET_ACCESS_KEY = acces-key
		AMAZON_REGION = eu-west-3
		AMAZON_BUCKET = bucketName


Examples
--------

Use this module like this:
	
.. code-block:: python

	# Imports
	import speechtotext
	from speechtotext.datasets import Dataset
	from speechtotext.benchmark.customBenchmarks import *
	from speechtotext.benchmark.benchmarks import run_benchmarks, Benchmark
	from speechtotext.functions import force_cudnn_initialization
	from speechtotext.plot.plotting import Plotting

	import speechtotext.metric.customMetrics
	force_cudnn_initialization()

	# Load dataset
	dataset = Dataset(path_to_dir="path/to/dataset", name= "dataset_name")

	# Settings and to run benchmarks
	number_of_samples = 100

	wb = WhisperBenchmark()
	wAPIb = WhisperAPIBenchmark()
	benchmark_list: list[Benchmark] = [wb, wAPIb]

	# Run benchmarks
	results = run_benchmarks(benchmark_list, dataset, number_of_samples)

	# Create plots
	plotting = Plotting(results=results, report_name = "benchmark_name")
	plotting.save_all()
