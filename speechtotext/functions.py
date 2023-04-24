"""Module with functions for the speechtotext package.
 
Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.functions import *
	
	# Force torch use for cuda
	force_cudnn_initialization()
	
	# Clean string
	string_cleaning("this has.//./8 to be cleaned::@")
"""

from functools import wraps
from time import time
import os
import re
import torch
import functools
import pandas as pd
from datetime import datetime
from abc import ABC, abstractmethod
from dotenv import load_dotenv

REGEX_STRING_PARSE:str = '[^A-Za-z0-9 ]+'
"""str: Regex used to clean the transcripts.
"""
DEFAULT_DATETIME_FORMAT:str = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
"""str: Default datetime format. (Uses string format for datetime)
"""
DEFAULT_REPORTS_FOLDER:str = "reports"
"""str: Default folder to save the reports.
"""
DEFAULT_CSV_NAME:str = f"{DEFAULT_REPORTS_FOLDER}/Benchmark_results_{DEFAULT_DATETIME_FORMAT}.csv"
"""str: Default path to save Benchmark results.
"""

def force_cudnn_initialization():
	"""Force torch use for cuda if available.
	"""    
	if torch.cuda.is_available():
		s = 32
		dev = torch.device('cuda')
		torch.nn.functional.conv2d(torch.zeros(s, s, s, s, device=dev), torch.zeros(s, s, s, s, device=dev))

def string_cleaning(text:str)-> str:
	"""Cleaning of string for STT.

	Args:
		text (str): Uncleaned string.

	Returns:
		str: Cleaned string.
	"""    
	return re.sub(REGEX_STRING_PARSE, '', text).rstrip()

def join_benchmark_results(results: list[pd.core.frame.DataFrame], set_index=True) -> pd.core.frame.DataFrame:
	"""Join Benchmark results.

	Args:
			results (list[pd.core.frame.DataFrame]): Results of benchmarks.
			set_index (bool, optional): Set True if ["model_name", "audio_ID"] can be set as index. Defaults to True.

	Returns:
			pd.core.frame.DataFrame: Dataframe with results of all benchmarks.
	"""
	df = pd.concat(results)
	if set_index:
		df = df.set_index(["model_name", "audio_ID"])
		return df
	return df.reset_index(drop=True)

def separate_benchmark_results_by_model(dataframe: pd.core.frame.DataFrame) -> dict[str, pd.core.frame.DataFrame]:
	"""Seperate benchmark results for each model.

	Args:
			dataframe pd.core.frame.DataFrame: Dataframe with results of all benchmarks.

	Returns:
			(list[pd.core.frame.DataFrame]): Results of benchmarks. 
	"""
	
	model_names = dataframe["model_name"].unique()

	DataFrameDict = {elem : pd.DataFrame() for elem in model_names}

	for key in DataFrameDict.keys():
		df = dataframe[:][dataframe["model_name"] == key]
		df = df.set_index("audio_ID")
		del df['model_name']
		DataFrameDict[key] = df
	
	return DataFrameDict

def benchmark_results_to_csv(results: list[pd.core.frame.DataFrame], save_name:str=DEFAULT_CSV_NAME):
	"""Creates csv from benchmark results.
	
	Args:
		results (list[pd.core.frame.DataFrame]): List of results from benchmarks.
		save_name (str, optional): Filename of output. Defaults to DEFAULT_CSV_NAME.
	"""  
	df = pd.concat(results)
	df.to_csv(save_name, index=False)
 
def save_sub_folder_name(folder_path:str, subfolder_name:str) -> str:
	"""Creates subfolder path.

	Args:
		folder_path (str): Path of parent folder.
		subfolder_name (str): Subfolder name.

	Returns:
		str: Path to save folder.
	"""    
	folder_name =  f"{folder_path}/{subfolder_name}"
	if not os.path.isdir(folder_name):
		os.makedirs(folder_name)
	return folder_name

def save_folder_name(report_name:str, folder_name:str = DEFAULT_REPORTS_FOLDER) -> str:
	"""Makes folder path.

	Args:
		report_name (str): Name of report.
		folder_name (str, optional): Name of folder. Defaults to DEFAULT_REPORT_FOLDER.

	Returns:
		str: path to save folder.
	"""    
	folder_name =  f"{folder_name}/{report_name}_{DEFAULT_DATETIME_FORMAT}"
	if not os.path.isdir(folder_name):
		os.makedirs(folder_name)
	return folder_name

class BaseResult(ABC):
	"""Parent class for results. 
 	Child class should be made and added to Plotting.CUSTOM_RESULTS, Plotting.CUSTOM_ERRORS, Plotting.CUSTOM_PLOTS or Plotting.CUSTOM_ERROR_PLOTS
	"""   
	def __init__(self, df:pd.core.frame.DataFrame, report_folder:str, file_name:str):
		"""Creates object of BaseResult. Child class should be added to Plotting.CUSTOM_RESULTS.

		Args:
			df (pd.core.frame.DataFrame): Dataframe that needs to be plotted.
			report_folder (str): Path to report folder.
			file_name (str): Name of saved File.
		"""     
		self.report_folder = report_folder
		self.file_name = file_name
		self.df = df
		self.save_file_name = f"{self.report_folder}/{self.file_name}{self.ext}"

	@abstractmethod
	def save(self):
		"""Saves Result to report folder.
		"""     
		pass

def get_extention_of_file_name(file_name:str)-> str:
	"""Get extention of file name.

	Args:
		file_name (str): File name.

	Returns:
		str: Extention of tile name.
	"""    
	_ , file_extension = os.path.splitext(file_name)
	return file_extension

def get_file_name_without_extention(file_name:str)-> str:
	"""Get extention of file name.

	Args:
		file_name (str): File name.

	Returns:
		str: Extention of tile name.
	"""    
	file_name, _ = os.path.splitext(file_name)
	return file_name

def uppercase_for_first_character_in_string(string:str) -> str:
	"""Return string where first character is uppercase.

	Args:
		string (str): String to process.

	Returns:
		str: String where first character is uppercase.
	"""    
	return  string[0].upper() + string[1:]

def multidispatch(*types):
	"""Allow for Method overloading for classes.
	"""    
	def register(function):
		name = function.__name__
		mm = multidispatch.registry.get(name)
		if mm is None:
			@functools.wraps(function)
			def wrapper(self, *args):
				types = tuple(arg.__class__ for arg in args) 
				function = wrapper.typemap.get(types)
				if function is None:
					raise TypeError("no match")
				return function(self, *args)
			wrapper.typemap = {}
			mm = multidispatch.registry[name] = wrapper
		if types in mm.typemap:
			raise TypeError("duplicate registration")
		mm.typemap[types] = function
		return mm
	return register
multidispatch.registry = {}

class RequiredEnvVariablesMissing(Exception):
	"""Exception when an required env variable is missing.
	"""    
	def __init__(self, env_name:str):     
				
		super().__init__(f"Required env variable {env_name} is missing.")

def load_env_variable(env_name:str)-> str:
	"""Loads and returns env variable.

	Args:
		env_name (str): .env key.

	Raises:
		RequiredEnvVariablesMissing: Prints the variable name if its missing.

	Returns:
		str: Value of the .env key.
	"""    
	load_dotenv()
	if env_name not in os.environ:
		raise RequiredEnvVariablesMissing(env_name)
	return os.getenv(env_name)

  
def timing(f):
	"""Functions used to time duration of function.
	"""    
	@wraps(f)
	def wrap(*args, **kw):
		ts = time()
		result = f(*args, **kw)
		te = time()
		return result, te-ts
	return wrap
