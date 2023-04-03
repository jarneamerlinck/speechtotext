Code Examples for speechtotext
==============================

This page is an collection of examples of how to use the package.

Full usage example
------------------

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

	whisperBenchmark = WhisperBenchmark()
	whisperAPIBenchmark = WhisperAPIBenchmark()
	benchmark_list: list[Benchmark] = [whisperBenchmark, whisperAPIBenchmark]

	# Run benchmarks
	results = run_benchmarks(benchmark_list, dataset, number_of_samples)

	# Create plots
	plotting = Plotting(results=results, report_name = "benchmark_name")
	plotting.save_all()
