import unittest

class TestImport(unittest.TestCase):
	def test_base_import(self):
		"""Test base import.
		"""    
		import speechtotext
	def test_datasets_import(self):
		"""Test datasets import.
		"""  
		import speechtotext.datasets
	def test_functions_import(self):
		"""Test functions import.
		"""  
		import speechtotext.functions
	def test_benchmark_import(self):
		"""Test benchmark import.
		"""  
		import speechtotext.benchmark
	def test_metric_import(self):
		"""Test metric import.
		"""  
		import speechtotext.metric
	def test_model_import(self):
		"""Test model import.
		"""  
		import speechtotext.model
	def test_plot_import(self):
		"""Test plot import.
		"""  
		import speechtotext.plot
