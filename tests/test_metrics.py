import unittest
from speechtotext.metric.metrics import Metrics

class TestMetrics(unittest.TestCase):
	def setUp(self) -> None:
		self.audio_id = "id001"
		self.duration = 4
  
	def test_metric(self):
		"""Test Metrics.
		"""		
		reference = "This is a test"
		hypothesis = "This was a test" 
		m = Metrics(reference, hypothesis, self.audio_id, self.duration, with_cleaning=False)

		self.assertEqual(m.audio_id, self.audio_id)
		self.assertEqual(m.duration, self.duration)
		self.assertEqual(m.insertions, 0)
		self.assertEqual(m.deletions, 0)
		self.assertEqual(m.substitutions, 1)
		self.assertEqual(m.wer, 1/4)
		self.assertEqual(m.mer, 1/4)
	
	def test_metric_with_cleaning(self):
		"""Test Metrics with_cleaning.
		"""		
		reference = "This is a test"
		hypothesis = "This was a test!!" 
		m = Metrics(reference, hypothesis, self.audio_id, self.duration, with_cleaning=True)

		self.assertEqual(m.audio_id, self.audio_id)
		self.assertEqual(m.duration, self.duration)
		self.assertEqual(m.insertions, 0)
		self.assertEqual(m.deletions, 0)
		self.assertEqual(m.substitutions, 1)
		self.assertEqual(m.wer, 1/4)
		self.assertEqual(m.mer, 1/4)



