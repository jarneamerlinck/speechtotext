import unittest
from speechtotext.model.modelWrapper import *

class TestMetrics(unittest.TestCase):
  
	def test_metric_ABC(self):
		"""Test ModelWrapper ABC error on object creation.
		"""		
		def raise_error():
			model = ModelWrapper()
		self.assertRaises(TypeError, raise_error)