"""Module that plots the metrics from the benchmarks.

Use this module like this:
	
.. code-block:: python

	# Create class
	from speechtotext.plot.plotting import BasePlot, Plotting
	class BoxPlotOfModelsWer(BasePlot):

		def create_plot(self) -> matplotlib.figure.Figure:
			plot = sns.boxplot(data=self.df, x="wer", y="model_name")
			fig = plot.get_figure()
			return fig

		def save_plot(self):    
			fig = self.create_plot()
			fig.savefig(self.save_file_name)
	# Add models to Plotting
	Plotting.CUSTOM_PLOTS.append(BoxPlotOfModelsWer)
"""
import pandas as pd
import dtale
from datetime import datetime
from abc import ABC, abstractmethod
import plotly
import os

from speechtotext.datasets import Dataset
from speechtotext.functions import join_benchmark_results, save_folder_name
from speechtotext.functions import DEFAULT_REPORTS_FOLDER


class BasePlot(ABC):
	"""Parent class for custom plots. Code can be generated from d-tale. Child class should be made and added to Plotting.CUSTOM_PLOTS.

	"""    
	def __init__(self, df:pd.core.frame.DataFrame, report_folder:str, plot_name:str):
		"""Creates object of BasePlot

		Args:
			df (pd.core.frame.DataFrame): dataframe that needs to be plotted
			report_folder (str): path to report folder
			plot_name (str): Name of plot
		"""     
		self.report_folder = report_folder
		self.plot_name = plot_name
		self.df = df
		self.save_file_name = f"{self.report_folder}/{self.plot_name}.png"
		self.engine = "auto"
	
	def save_plot(self):
		"""Saves plot to folder.
		"""     
		plot = self.create_plot()
		self.plot = plot
		plot.write_image(file =self.save_file_name, validate=False, engine= self.engine)

	@abstractmethod
	def create_plot(self) -> plotly.graph_objs._figure.Figure:
		"""Creates plot to be saved.

		Returns:
			plotly.graph_objs._figure.Figure: Plot that needs to be saved.
		"""     
		pass

class Plotting():
	"""Class that is used to create plots for an benchmark.
	"""    
	CUSTOM_PLOTS: list[BasePlot] = []

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
		[custom_plot_class(self.df_with_all_cols, self.save_folder, custom_plot_class.__name__).save_plot() for custom_plot_class in self.CUSTOM_PLOTS]
