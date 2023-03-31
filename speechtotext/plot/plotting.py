"""Module that plots the results from the benchmarks.

Use this module like this:
	
.. code-block:: python

	# Imports
	from speechtotext.plot.plotting import BasePlot, Plotting	
 
	# Create plotting object
	plotting = Plotting(results=results, report_name = "report_name")
 
	# Create all custom plots that are added to Plotting.CUSTOM_PLOTS
	plotting.save_all()
 
"""
import pandas as pd
from abc import ABC, abstractmethod
import plotly
import matplotlib
import dtale

from speechtotext.functions import join_benchmark_results, save_folder_name, BaseResult
from speechtotext.functions import DEFAULT_REPORTS_FOLDER

class BasePlotly(BaseResult):
	"""Parent class for custom plots with Plotly. Code can be generated from d-tale. Child class should be made and added to Plotting.CUSTOM_RESULTS.

	"""    
	def __init__(self, df:pd.core.frame.DataFrame, report_folder:str, file_name:str):
		"""Creates object of BasePlot.

		Args:
			df (pd.core.frame.DataFrame): dataframe that needs to be plotted.
			report_folder (str): path to report folder.
			plot_name (str): Name of plot.
		"""     	
		self.ext = ".png"
		self.engine = "auto"
		super().__init__(df, report_folder, file_name) 
	
	def save(self):
		"""Saves plot to folder.
		"""     
		fig = self.create_plot()
		fig.write_image(file =self.save_file_name, validate=False, engine= self.engine)

	@abstractmethod
	def create_plot(self) -> plotly.graph_objs._figure.Figure:
		"""Creates plot to be saved.

		Returns:
			plotly.graph_objs._figure.Figure: Plot that needs to be saved.
		"""     
		pass

class BaseMatPlotLib(BaseResult):
	"""Parent class for custom plots with matplotlib. Child class should be made and added to Plotting.CUSTOM_RESULTS.

	"""    
	def __init__(self, df:pd.core.frame.DataFrame, report_folder:str, file_name:str):
		"""Creates object of BasePlot.

		Args:
			df (pd.core.frame.DataFrame): dataframe that needs to be plotted.
			report_folder (str): path to report folder.
			plot_name (str): Name of plot.
		"""     	
		self.ext = ".png"
		super().__init__(df, report_folder, file_name) 
	
	def save(self):
		"""Saves plot to folder.
		""" 
		fig = self.create_plot()
		fig.savefig(self.save_file_name)

	@abstractmethod
	def create_plot(self) -> matplotlib.figure.Figure:
		"""Creates plot to be saved.

		Returns:
			plotly.graph_objs._figure.Figure: Plot that needs to be saved.
		"""     
		pass

class Plotting():
	"""Class that is used to create plots for an benchmark.
	"""    
	CUSTOM_RESULTS: list[BaseResult] = []

	def __init__(self, results:list[pd.core.frame.DataFrame], report_name:str):
		self.report_name = report_name
		self.save_folder = save_folder_name(report_name)
		self.df = join_benchmark_results(results)
		self.df_with_all_cols = join_benchmark_results(results, set_index=False)
	
	def launch_dtale(self):
		"""Launch webui to explore the data.
		"""     
		d = dtale.show(self.df, hide_header_editor=False)
		d.open_browser()
  
	def save_all(self):
		"""Loops over all customPlot classes in CUSTOM_PLOTS to creates and saves the plots.
		"""     
		import speechtotext.plot.customPlots
		[custom_plot_class(self.df_with_all_cols, self.save_folder, custom_plot_class.__name__).save() for custom_plot_class in self.CUSTOM_RESULTS]
