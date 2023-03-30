"""Module with functions for the speechtotext package.
 
Use this module like this:
	
.. code-block:: python

	# Imports
 	from speechtotext.functions import *
	
	# Force torch use for cuda
	force_cudnn_initialization()
	
	# Clean string
	string_cleaning("this has.//./8 to be cleaned::@")

Attributes:
	REGEX_STRING_PARSE (str): Regex string parce used to clean up transcripts that are used to validate the speechtotext models.
"""

import threading
import os
import re
import torch
import functools
import pandas as pd
from datetime import datetime

REGEX_STRING_PARSE = '[^A-Za-z0-9 ]+'
DEFAULT_REPORT_FOLDER = "reports"
DEFAULT_CSV_NAME = f"{DEFAULT_REPORT_FOLDER}/Benchmark_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
DEFAULT_HTML_NAME = f"{DEFAULT_REPORT_FOLDER}/Benchmark_results_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"
DEFAULT_HTML_TITLE = f"{DEFAULT_REPORT_FOLDER}/Benchmark results of {datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"


def force_cudnn_initialization():
	"""Force torch use for cuda.
	"""    
	s = 32
	dev = torch.device('cuda')
	torch.nn.functional.conv2d(torch.zeros(s, s, s, s, device=dev), torch.zeros(s, s, s, s, device=dev))

def string_cleaning(text:str)-> str:
	"""Cleaning of string for STT.

	Args:
		text (str): uncleaned string.

	Returns:
		str: cleaned string.
	"""    
	return re.sub(REGEX_STRING_PARSE, '', text)

def join_benchmark_results(results: list[pd.core.frame.DataFrame], set_index=True) -> pd.core.frame.DataFrame:
	"""Join Benchmark results.

	Args:
			results (list[pd.core.frame.DataFrame]): results of benchmarks.
			set_index (bool, optional): Set True if ["model_name", "audio_ID"] can be set as index. Defaults to True.

	Returns:
			pd.core.frame.DataFrame: Dataframe with results of all benchmarks.
	"""
	df = pd.concat(results)
	if set_index:
		df = df.set_index(["model_name", "audio_ID"])
	return df

def separate_benchmark_results_by_model(dataframe: pd.core.frame.DataFrame) -> dict[str, pd.core.frame.DataFrame]:
	"""Seperate benchmark results for each model.

	Args:
			dataframe pd.core.frame.DataFrame: Dataframe with results of all benchmarks.

	Returns:
			(list[pd.core.frame.DataFrame]): results of benchmarks. 
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
		save_name (str, optional): filename of output. Defaults to DEFAULT_CSV_NAME.
	"""  
	df = pd.concat(results)
	df.to_csv(save_name, index=False)
 
def benchmark_results_to_html(dict_results: dict[str, pd.core.frame.DataFrame], title:str = DEFAULT_HTML_TITLE, save_name: str = DEFAULT_HTML_NAME):
	"""Saves benchmark results to html overview.

	Args:
		results (list[pd.core.frame.DataFrame]): List of results from benchmarks.
		title (str, optional): Title on the report. Defaults to DEFAULT_HTML_TITLE.
		save_name (str, optional): filename of the output. Defaults to DEFAULT_HTML_NAME.
	"""    
	reports = []
	for _, (key, df) in enumerate(dict_results.items()):
		print(key, df.columns)
		raport = ProfileReport(df, title=key)
		raport.to_file(f"benchmark_results_{key}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html")
		reports.append(raport)
	
	# comparison_report = compare(reports[0:max])
	# statistics = comparison_report.get_description()
	# comparison_report.to_file(save_name)
 
def save_benchmark_results(results: list[pd.core.frame.DataFrame]):
	"""Save benchmark results to csv and html.

	Args:
		results (list[pd.core.frame.DataFrame]): List of results.
	"""
	df = join_benchmark_results(results, set_index=False)
	dict_of_dfs = separate_benchmark_results_by_model(df)
	benchmark_results_to_html(dict_of_dfs)
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

