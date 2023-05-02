"""Module to create custom metrics to save with the plots from the plotting module.

Use this module like this:
	
.. code-block:: python

	# Imports
	from speechtotext.functions import BaseResult
	from speechtotext.plot.plotting import Plotting
 
	# Create class with matplotlib picture
	class BenchmarkResults(BaseMetrics):
		def create_df(self) -> pd.core.frame.DataFrame:
			return self.df

	# Add model to Plotting
	Plotting.CUSTOM_RESULTS.append(BenchmarkResults)
"""

import pandas as pd
import numpy as np
from abc import abstractmethod

from speechtotext.metric.metrics import *
from speechtotext.functions import BaseResult
from speechtotext.plot.plotting import Plotting

class BaseMetrics(BaseResult):
	"""Base class used to create metrics for result dataframe.
	"""    
	def __init__(self, df: pd.core.frame.DataFrame, report_folder: str, file_name: str):
		self.ext = ".csv"
		super().__init__(df, report_folder, file_name)

	def save(self):
		df_result = self.create_df()
		df_result.to_csv(self.save_file_name, index=False)

	@abstractmethod
	def create_df(self) -> pd.core.frame.DataFrame:
		"""Creates df that needs to be saved.

		Returns:
			pd.core.frame.DataFrame: Dataframe that needs to be saved.
		"""	  
		pass

class BenchmarkResults(BaseMetrics):
	"""This class saves the results of the benchmark.
	"""    
	def create_df(self) -> pd.core.frame.DataFrame:
		return self.df
# Add metrics to Plotting
Plotting.CUSTOM_RESULTS.append(BenchmarkResults)

class ResultMetrics(BaseMetrics):
	"""This class calulates the default statistic metrics on the benchmark results.
	"""    
	def create_df(self) -> pd.core.frame.DataFrame:
		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)

		# remove any pre-existing indices for ease of use in the D-Tale code, but this is not required
		df = df.reset_index().drop('index', axis=1, errors='ignore')
		df.columns = [str(c) for c in df.columns]  # update columns to strings in case they are numbers

		list_of_df = []
		for metric_name in ["wer", "mer", "wil", "wip", "cer"]:
			df = df[[c for c in df.columns if c not in ['reference']]]
			# main statistics
			stats = df[metric_name].describe().to_frame().T
			stats['sum'] = df[metric_name].sum()
			stats['median'] = df[metric_name].median()
			mode = df[metric_name].mode().values
			stats['mode'] = np.nan if len(mode) > 1 else mode[0]
			stats['var'] = df[metric_name].var()
			stats['sem'] = df[metric_name].sem()

			sequential_diffs = df[metric_name].diff()

			stats['min_diff']  = sequential_diffs.min()
			stats['max_diff']  = sequential_diffs.max()
			stats['avg_diff']  = sequential_diffs.mean()
			stats['diff_vals']  = sequential_diffs.value_counts().sort_values(ascending=False)

			columnsTitlesOrder = ['count', 'unique','top', 'freq', 'sum', 'median', 'mode', 'var', 'sem', 'min_diff', 'max_diff', 'avg_diff', 'diff_vals']

			stats = stats.reindex(columns=columnsTitlesOrder)
			list_of_df.append(stats)
		
		return pd.concat(list_of_df)
# Add metrics to Plotting
Plotting.CUSTOM_RESULTS.append(ResultMetrics)

class ErrorMetrics(BaseMetrics):
	"""This class calulates the error statistic on the benchmark results.
	"""    
	def create_df(self) -> pd.core.frame.DataFrame:
		pass
# Add metrics to Plotting

# Plotting.CUSTOM_ERRORS.append(ErrorMetrics)

