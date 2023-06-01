import unittest
from speechtotext.model.modelWrapper import *

class TestModels(unittest.TestCase):
  
	def test_model_ABC_Error(self):
		"""Test ModelWrapper ABC error on object creation.
		"""		
		def raise_error():
			model = ModelWrapper()
		self.assertRaises(TypeError, raise_error)