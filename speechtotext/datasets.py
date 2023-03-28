from os.path import exists
import pandas as pd

class DatasetBare():
	"""Bare dataset class 
	"""    
	def __init__(self, path_to_dir:str, name: str, file_ext:str=".wav"):
		"""Creates dataset object.
		There needs to be an transcript.txt directly in the dir.
		Args:
			path_to_dir (str): path to dir ending with "/".
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
			id (str): id of file.

		Raises:
			FileNotFoundError: if id doesn't exist.

		Returns:
			str: Path to fragment.
		"""     
		path = f"{self.path_to_dir}{id}{self.file_ext}"

		if exists(path):
			return path
		else:
			raise FileNotFoundError()
		 
	def get_text_of_id(self, id:str) -> str:
		"""Get text of fragment id.

		Args:
			id (str): id of fragment.

		Returns:
			str: string of spoken text.
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
		self.dataset = df

class Dataset(DatasetBare):
	def __init__(self, path_to_dir:str, name: str, file_ext:str=".wav"):  
		super().__init__(path_to_dir, name, file_ext)
		self.load_transcript()

	def load_transcript(self):
		"""Loads transcript.
		"""     
		file_path = f"{self.path_to_dir}transcripts.txt"

		df= pd.read_csv(file_path, sep="|", header=None)
		df = df.iloc[:, 0:2] 
		df.columns = ["id", "text"]
		self.dataset = df

	def get_n_samples(self, number_of_samples:int) -> SampleDataset:
		"""Get n random samples.

		Args:
			number_of_samples (int): Number of random samples.

		Returns:
			SampleDataset: dataset with the samples.
		"""     
		if number_of_samples > self.number_of_samples():
			print("number larger then samples in dataset. Using full dataset")
			number_of_samples = self.dataset.number_of_samples()
		df = self.dataset.sample(n=number_of_samples)

		return SampleDataset(df, self.path_to_dir, self.name, self.file_ext)
