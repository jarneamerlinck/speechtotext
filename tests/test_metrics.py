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

	def test_metric_with_deletions(self):
		"""Test Metrics with_cleaning.
		"""		
		reference = "This is a test for the best"
		hypothesis = "This is a test the best" 
		m = Metrics(reference, hypothesis, self.audio_id, self.duration, with_cleaning=False)

		self.assertEqual(m.audio_id, self.audio_id)
		self.assertEqual(m.duration, self.duration)
		self.assertEqual(m.insertions, 0)
		self.assertEqual(m.deletions, 1)
		self.assertEqual(m.substitutions, 0)
		self.assertEqual(m.wip, 6/7)
		self.assertEqual(m.cer, 4/27)

	def test_metric_in_all_metrics(self):
		"""Test get_all_metric_names.
		"""	
		reference = "This is a test for the best"
		hypothesis = "This is a test the best" 
		m = Metrics(reference, hypothesis, self.audio_id, self.duration, with_cleaning=False)
		list_of_metrics = Metrics.get_all_metric_names()

		list_of_to_test_metrics = ["cer", "wil", "wip", "deletions", "insertions", "duration"]
		[self.assertIn(metric, list_of_metrics) for metric in list_of_to_test_metrics]

	def test_metric_in_all_metric_docs(self):
		"""Test get_all_metric_docs.
		"""	
		reference = "This is a test for the best"
		hypothesis = "This is a test the best" 
		m = Metrics(reference, hypothesis, self.audio_id, self.duration, with_cleaning=False)
		list_of_metrics_names = Metrics.get_all_metric_names()
		list_of_metrics_description = Metrics.get_all_metric_docs()

		list_of_to_test_metrics = ["cer", "wil", "wip", "deletions", "insertions", "duration"]
		[self.assertIn(metric_name, desc.lower()) for metric, desc in zip(list_of_metrics_names, list_of_metrics_description) for metric_name in list_of_to_test_metrics if metric == metric_name]

	def test_print(self):
		"""Test get_all_metric_docs.
		"""	
		reference = "This is a test for the best"
		hypothesis = "This is a test the best" 
		m = Metrics(reference, hypothesis, self.audio_id, self.duration, with_cleaning=False)
		to_print = f"wer: {1/7}, mer: {1/7}, wil: {1- 6/7}, wip: {6/7}, cer: {4/27}"
		self.assertEqual(to_print, str(m))

	def test_lenght_of_metric_names(self):
		"""Test get_all_metric_docs and get_all_metric_names.
		"""
		self.assertEqual(Metrics.get_all_metric_names().__len__(), Metrics.get_all_metric_docs().__len__())