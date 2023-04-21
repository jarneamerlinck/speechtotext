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
import itertools

from speechtotext.metric.metrics import Metrics
from speechtotext.functions import join_benchmark_results, save_folder_name, save_sub_folder_name, BaseResult, benchmark_results_to_csv, uppercase_for_first_character_in_string
from speechtotext.functions import DEFAULT_REPORTS_FOLDER

class BasePlotly(BaseResult):
	"""Parent class for custom plots with Plotly. Code can be generated from d-tale. Child class should be made and added to Plotting.CUSTOM_RESULTS.

	"""    
	def __init__(self, df:pd.core.frame.DataFrame, report_folder:str, file_name:str):
		"""Creates object of BasePlot.

		Args:
			df (pd.core.frame.DataFrame): Dataframe that needs to be plotted.
			report_folder (str): Path to report folder.
			file_name (str): Name of plot.
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
			df (pd.core.frame.DataFrame): Dataframe that needs to be plotted.
			report_folder (str): Path to report folder.
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

class DynamicallyCreatePlotClassesByMetricByDatabase(BaseResult):
	"""Dynamically create plot classes for each metric for each database in the given dataframe. This class is a parent class. The child class should be added to Plotting.CUSTOM_PLOTS.

	"""    
	def __init__(self, df: pd.core.frame.DataFrame, report_folder: str, file_name: str):
		"""Creates object of class.

		Args:
			df (pd.core.frame.DataFrame): Dataframe that needs to be plotted.
			report_folder (str): Path to report folder.
			file_name (str): Name of plot.
		"""     
		self.ext = ".png"
		self.PLOT_CLASS_NAME_LIST = []
		super().__init__(df, report_folder, file_name)
	
	def create_plot_classes(self):
		"""Creates plot classes.
		"""     
		list_of_metric_names:list[str] = Metrics.get_all_metric_names()

		list_of_metric_description:list[str] = Metrics.get_all_metric_docs()
		list_of_dataset_names:list[str] = Plotting.DATASET_NAMES
		
		for (metric_name, metric_description), dataset_name in itertools.product(zip(list_of_metric_names, list_of_metric_description), list_of_dataset_names):
	 
			class_name = f"{uppercase_for_first_character_in_string(metric_name)}ByModelnameFor{uppercase_for_first_character_in_string(dataset_name)}"

			class_type = type(class_name, (BasePlotly, ), dict(	
					# data members
					metric_name= metric_name,
					metric_description= metric_description,
					dataset_name= dataset_name,
					ext= self.ext,
					# Methodes to override
					create_plot= self.__class__.create_plot,
			))
			# Add to to plot list 
			self.PLOT_CLASS_NAME_LIST.append(class_type)


	def save(self):
		"""Saves plot to folder.
		"""  
		self.create_plot_classes()
		[custom_results_class(self.df, self.report_folder, custom_results_class.__name__).save() for custom_results_class in self.PLOT_CLASS_NAME_LIST]
	
	@abstractmethod
	def create_plot(self):
		pass


class Plotting():
	"""Class that is used to create plots for an benchmark.
	"""    
	CUSTOM_RESULTS: list[BaseResult] = []
	CUSTOM_ERRORS: list[BaseResult] = []
	CUSTOM_PLOTS: list[BaseResult] = []
	CUSTOM_ERROR_PLOTS: list[BaseResult] = []
	DATASET_NAMES: list[str] = []

	def __init__(self, results:list[pd.core.frame.DataFrame], errors:list[pd.core.frame.DataFrame],report_name:str):
		"""Creates plotting object

		Args:
			results (list[pd.core.frame.DataFrame]): List of result dataframes.
			errors (list[pd.core.frame.DataFrame]): List of error dataframes.
			report_name (str): Name of report.
		"""     
		self.report_name = report_name

		self.save_folder = save_folder_name(f"{report_name}")
		self.save_plot_folder = save_sub_folder_name(self.save_folder, "plots")
		self.save_error_folder = save_sub_folder_name(self.save_folder, "error_plots")

		self.df = join_benchmark_results(results)
		self.df_with_all_cols = join_benchmark_results(results, set_index=False)
		self.error_df = join_benchmark_results(errors, set_index=False)
		benchmark_results_to_csv(errors, save_name= f"{self.save_folder}/errors.csv")
		
		Plotting.DATASET_NAMES = pd.concat([self.df, self.error_df])["dataset"].unique().tolist()		
	
	def launch_dtale(self):
		"""Launch webui to explore the data.
		"""     
		d = dtale.show(self.df, hide_header_editor=False)
		d.open_browser()
  
	def save_all(self):
		"""Loops over all customPlot classes in CUSTOM_PLOTS to creates and saves the plots.
		"""     
		import speechtotext.plot.customPlots
		import speechtotext.plot.customErrorPlots
		import speechtotext.metric.customMetrics
  		# Results
		[custom_results_class(self.df_with_all_cols, self.save_folder, custom_results_class.__name__).save() for custom_results_class in self.CUSTOM_RESULTS]
		[custom_plot_class(self.df_with_all_cols, self.save_plot_folder, custom_plot_class.__name__).save() for custom_plot_class in self.CUSTOM_PLOTS]

		# Errors
		[custom_plot_class(self.error_df, self.save_error_folder, custom_plot_class.__name__).save() for custom_plot_class in self.CUSTOM_ERROR_PLOTS]
		[custom_results_class(self.error_df, self.save_folder, custom_results_class.__name__).save() for custom_results_class in self.CUSTOM_ERRORS]
	