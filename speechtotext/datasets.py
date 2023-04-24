"""Module to create the datasets for the speechtotext package.

The dataset requires an ``transcripts.txt`` in the dataset folder. In there are relative links to the audiofiles followed by ``|`` and the transcript of that file.

Example of entry::

	20000_mijlen/20000_mijlen_0001.wav|This is the trancsript of the audio

Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.datasets import Dataset
	from speechtotext.benchmarks import *
	
	# Settings
	path_to_dir = "path/to/dir"
	dataset_name = "dataset_name"
	id = "existing_id"
	number_of_samples = 10
	
	# Create dataset
	dataset = Dataset(path_to_dir=path_to_dir, name= dataset_name)
 
	# Print number of samples
	print(dataset.number_of_samples())
 
	# Get audio file from id
	dataset.get_path_of_fragment(id)
 
	# Get transcript from id
	dataset.get_text_of_id(id)
	
	# Get n trandom samples
	dataset_n_random: SampleDataset = dataset.get_n_samples(number_of_samples)
"""

from os.path import exists
import pandas as pd

from speechtotext.functions import get_file_name_without_extention

class DatasetBare():
	"""Bare dataset class.
	"""    
	def __init__(self, path_to_dir:str, name: str, file_ext:str=".wav"):
		"""Creates dataset object.
		There needs to be an transcripts.txt directly in the dir.
		Args:
			path_to_dir (str): Path to dir ending with "/".
			name (str): Name of dataset.
			file_ext (str): Extention of files.
		"""     
		self.name = name
		self.path_to_dir = path_to_dir
		self.file_ext = file_ext

	def number_of_samples(self) -> int:
		"""Get number of samples in dataset.

		Returns:
			int: Number of samples in dataset.
		"""     
		return self.dataset.shape[0]
  
	def get_path_of_fragment(self, id:str)-> str:
		"""Gets path of fragment.

		Args:
			id (str): Id of file.

		Raises:
			FileNotFoundError: If id doesn't exist.

		Returns:
			str: Path to fragment.
		"""     
		path = f"{self.path_to_dir}/{id}{self.file_ext}"

		if exists(path):
			return path
		else:
			raise FileNotFoundError()
		 
	def get_text_of_id(self, id:str) -> str:
		"""Get text of fragment id.

		Args:
			id (str): Id of fragment.

		Returns:
			str: String of spoken text.
		"""     
		row = self.dataset[self.dataset["id"] == id]
		try:
			return row.values[0][1]
		except:
			return None

class SampleDataset(DatasetBare):
	"""Sample of dataset.
	"""    
	def __init__(self, df: pd.core.frame.DataFrame, path_to_dir: str, name: str, file_ext: str = ".wav"):
		super().__init__(path_to_dir, name, file_ext)
		self.dataset: pd.core.frame.DataFrame = df

class Dataset(DatasetBare):
	"""Class to extract data from the dataset folder.
	"""    
	def __init__(self, path_to_dir:str, name: str, file_ext:str=".wav"):  
		super().__init__(path_to_dir, name, file_ext)
		self.load_transcript()

	def load_transcript(self):
		"""Loads transcript.
		"""     
		file_path = f"{self.path_to_dir}/transcripts.txt"

		df= pd.read_csv(file_path, sep="|", header=None)
		df = df.iloc[:, 0:2] 
		df.columns = ["id", "text"]
		df['id'] = df['id'].apply(lambda id :get_file_name_without_extention(id) )
		self.dataset: pd.core.frame.DataFrame = df

	def get_n_samples(self, number_of_samples:int) -> SampleDataset:
		"""Get n random samples.

		Args:
			number_of_samples (int): Number of random samples.

		Returns:
			SampleDataset: Dataset with the samples.
		"""     
		if number_of_samples > self.number_of_samples():
			print("number larger then samples in dataset. Using full dataset")
			number_of_samples = self.number_of_samples()
		df = self.dataset.sample(n=number_of_samples)

		return SampleDataset(df, self.path_to_dir, self.name, self.file_ext)
