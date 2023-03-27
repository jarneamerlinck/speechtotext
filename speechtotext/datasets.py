from os.path import exists
import pandas as pd


class Dataset():
	def __init__(self, dir:str, file_ext:str=".wav"):
		"""Creates dataset object
		There needs to be an transcript.txt directly in the dir
		Args:
			dir (str): path to dir ending with /
			file_ext (str): Extention of files
		"""     
		self.path_to_dir = dir
		self.file_ext = file_ext
		self.load_transcript()

	def load_transcript(self):
		"""Loads transcript
		"""     
		file_path = f"{self.path_to_dir}transcripts.txt"

		df= pd.read_csv(file_path, sep="|", header=None)
		df = df.iloc[:, 0:2] 
		df.columns = ["id", "text"]
		#self.transcript = df.set_index('id') , names=
		self.transcript = df
  
	def get_path_of_fragment(self, id:str)-> str:
		"""Gets path of fragment

		Args:
			id (str): id of file

		Raises:
			FileNotFoundError: if id doesn't exist

		Returns:
			str: _description_
		"""     
		path = f"{self.path_to_dir}{id}{self.file_ext}"

		if exists(path):
			return path
		else:
			raise FileNotFoundError()
		 

	def get_text_of_id(self, id:str) -> str:
		"""Get text of fragment id

		Args:
			id (str): id of fragment

		Returns:
			str: string of spoken text
		"""     
		row = self.transcript[self.transcript["id"] == id]
		try:
			return row.values[0][1]
		except:
			return None