import unittest

class TestDatasetsWithoutTranscript(unittest.TestCase):
	def setUp(self) -> None:
		import os
		self.dataset_folder =  "test_dataset_folder"
		if not os.path.isdir(self.dataset_folder):
			os.makedirs(self.dataset_folder)
	def tearDown(self):
		import shutil, os
		shutil.rmtree(self.dataset_folder)
		self.assertFalse(os.path.isdir(self.dataset_folder))
	
	def test_init(self):
		"""Test no transcript error.
		"""     
		from speechtotext.datasets import Dataset
		def raise_error():
			d = Dataset(self.dataset_folder, "name", file_ext:=".wav")
		self.assertRaises(FileNotFoundError, raise_error)

class TestDatasetsWithTranscripts(TestDatasetsWithoutTranscript):
	def setUp(self) -> None:
		super().setUp()
		toWrite = """id001|Dit is een transcript
id002|Hiermee geen hulp.
id003|Alles van de testen slagen zonder problemen!"""
		with open(f"{self.dataset_folder}/transcripts.txt", "w") as text_file:
			text_file.write(toWrite)
		file_ext = ".wav"
		for id in ["id001", "id002", "id003"]:
			open(f"{self.dataset_folder}/{id}{file_ext}", 'a').close()
	
	def test_init(self):
		"""Test with transcript error.
		"""     
		from speechtotext.datasets import Dataset
		d = Dataset(self.dataset_folder, "name", file_ext:=".wav")

	def test_load_transcript(self):
		"""Test test_load_transcript.
		"""  
		from speechtotext.datasets import Dataset
		d = Dataset(self.dataset_folder, "name", file_ext:=".wav")
		d.load_transcript()
	
	def test_get_n_samples_smaller(self):
		"""Test get_n_samples.
		"""  
		from speechtotext.datasets import Dataset, SampleDataset
		d = Dataset(self.dataset_folder, "name", file_ext:=".wav")
		number_of_samples = 1
		samples = d.get_n_samples(number_of_samples)
		self.assertIsInstance(samples, SampleDataset)
		self.assertEqual(number_of_samples, samples.dataset.shape[0])

	def test_get_n_samples_same(self):
		"""Test get_n_samples.
		"""  
		from speechtotext.datasets import Dataset, SampleDataset
		d = Dataset(self.dataset_folder, "name", file_ext:=".wav")
		number_of_samples = 3
		samples = d.get_n_samples(number_of_samples)
		self.assertIsInstance(samples, SampleDataset)
		self.assertEqual(number_of_samples, samples.dataset.shape[0])
	
	def test_get_n_samples_larger(self):
		"""Test get_n_samples.
		"""  
		from speechtotext.datasets import Dataset, SampleDataset
		d = Dataset(self.dataset_folder, "name", file_ext:=".wav")
		number_of_samples = 5
		max_samples = d.dataset.shape[0]
		samples = d.get_n_samples(number_of_samples)
		self.assertIsInstance(samples, SampleDataset)
		self.assertEqual(max_samples, samples.dataset.shape[0])
	
	def test_get_path_of_fragment(self):
		"""Test get_path_of_fragment.
		"""  
		from speechtotext.datasets import Dataset, SampleDataset
		file_ext =".wav"
		d = Dataset(self.dataset_folder, "name", file_ext=file_ext)
		id = "id001"
		correct_path = f"{self.dataset_folder}/{id}{file_ext}"
		self.assertEqual(correct_path, d.get_path_of_fragment(id))
	
	def test_get_text_of_id(self):
		"""Test get_text_of_id.
		"""  
		from speechtotext.datasets import Dataset, SampleDataset
		file_ext =".wav"
		d = Dataset(self.dataset_folder, "name", file_ext=file_ext)
		id = "id003"
		correct_text= "Alles van de testen slagen zonder problemen!"
		self.assertEqual(correct_text, d.get_text_of_id(id))

	def test_get_text_of_id_with_sample(self):
		"""Test get_text_of_id.
		"""  
		from speechtotext.datasets import Dataset, SampleDataset
		file_ext =".wav"
		d = Dataset(self.dataset_folder, "name", file_ext=file_ext)
		sample = d.get_n_samples(3)
		id = "id003"
		correct_text= "Alles van de testen slagen zonder problemen!"
		self.assertEqual(correct_text, sample.get_text_of_id(id))