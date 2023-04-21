"""Module to create custom plots for the plotting module

Use this module like this:
	
.. code-block:: python

	# Imports
	from speechtotext.functions import BaseResult
	from speechtotext.plot.plotting import Plotting
 
	# Create class with matplotlib picture
	class BoxPlotOfModelsWer(BasePlot):

		def create_plot(self) -> matplotlib.figure.Figure:
			plot = sns.boxplot(data=self.df, x="wer", y="model_name")
			fig = plot.get_figure()
			return fig

		def save_plot(self):    
			fig = self.create_plot()
			fig.savefig(self.save_file_name)
	# Add model to Plotting
	Plotting.CUSTOM_PLOTS.append(BoxPlotOfModelsWer)

	# Create class with plotly picture
	from speechtotext.plot.plotting import BasePlot, Plotting
	class DemoPlotlyExample(BasePlot):

		def create_plot(self) -> plotly.graph_objs._figure.Figure:
			self.df = px.data.gapminder().query("country=='Canada'")
			fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
			return fig

	# Add model to Plotting
	Plotting.CUSTOM_PLOTS.append(DemoPlotlyExample)
"""
import plotly
import plotly.express as px
import plotly.tools as tls
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import matplotlib


from speechtotext.plot.plotting import BasePlotly, Plotting, BaseMatPlotLib, DynamicallyCreatePlotClassesByMetricByDatabase
from speechtotext.functions import  BaseResult
from speechtotext.metric.metrics import Metrics

class CerByModelnameByDataset(BasePlotly):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
   
		y_name = "cer"

		chart_data = pd.concat([
			df['model_name'],
			df[y_name],
			df['dataset'],
		], axis=1)

		figure = px.box(chart_data, x="model_name", y=y_name, color="dataset")
		for s in df["model_name"].unique():
			figure.add_annotation(x=s,
							y = df[df['model_name']==s][y_name].max(),
							text = f"{len(df[df['model_name']==s]['model_name'])}",
							yshift = 10,
							showarrow = False
							)
		figure.update_layout(
			title={
				'text': self.__class__.__name__,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			showlegend=True)
		y_title = [string for string in Metrics.get_all_metric_docs() if y_name.upper() in string][0]
		figure.update_yaxes(
      		title=y_title)
		return figure
# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(CerByModelnameByDataset)

class WerByModelnameByDataset(BasePlotly):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
   
		y_name = "wer"

		chart_data = pd.concat([
			df['model_name'],
			df[y_name],
			df['dataset'],
		], axis=1)

		figure = px.box(chart_data, x="model_name", y=y_name, color="dataset")
		for s in df["model_name"].unique():
			figure.add_annotation(x=s,
							y = df[df['model_name']==s][y_name].max(),
							text = f"{len(df[df['model_name']==s]['model_name'])}",
							yshift = 10,
							showarrow = False
							)
		figure.update_layout(
			title={
				'text': self.__class__.__name__,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			showlegend=True)
		y_title = [string for string in Metrics.get_all_metric_docs() if y_name.upper() in string][0]
		figure.update_yaxes(
      		title=y_title)
		return figure
# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(WerByModelnameByDataset)

class DurationByModelnameByDataset(BasePlotly):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
   
		y_name = "duration"

		chart_data = pd.concat([
			df['model_name'],
			df[y_name],
			df['dataset'],
		], axis=1)

		figure = px.box(chart_data, x="model_name", y=y_name, color="dataset")
		for s in df["model_name"].unique():
			figure.add_annotation(x=s,
							y = df[df['model_name']==s][y_name].max(),
							text = f"{len(df[df['model_name']==s]['model_name'])}",
							yshift = 10,
							showarrow = False
							)

		figure.update_layout(
			title={
				'text': self.__class__.__name__,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			showlegend=True)
		y_title = [string for string in Metrics.get_all_metric_docs() if y_name in string][0]
		figure.update_yaxes(
      		title=y_title)
		return figure
# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(DurationByModelnameByDataset)

class DurationLogByModelnameByDataset(BasePlotly):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
   
		y_name = "duration"

		chart_data = pd.concat([
			df['model_name'],
			df[y_name],
			df['dataset'],
		], axis=1)

		figure = px.box(chart_data, x="model_name", y=y_name, color="dataset", log_y=True)
		for s in df["model_name"].unique():
			figure.add_annotation(x=s,
							y = df[df['model_name']==s][y_name].max(),
							text = f"{len(df[df['model_name']==s]['model_name'])}",
							yshift = 10,
							showarrow = False
							)
   
		figure.update_layout(
			title={
				'text': self.__class__.__name__,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			yaxis_title = "duration (log)",
			showlegend=True)
		y_title = [string for string in Metrics.get_all_metric_docs() if y_name in string][0]
		figure.update_yaxes(
      		title=y_title)
		return figure
# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(DurationLogByModelnameByDataset)

class MerByModelnameByDataset(BasePlotly):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
   
		y_name = "mer"

		chart_data = pd.concat([
			df['model_name'],
			df[y_name],
			df['dataset'],
		], axis=1)

		figure = px.box(chart_data, x="model_name", y=y_name, color="dataset")
		for s in df["model_name"].unique():
			figure.add_annotation(x=s,
							y = df[df['model_name']==s][y_name].max(),
							text = f"{len(df[df['model_name']==s]['model_name'])}",
							yshift = 10,
							showarrow = False
							)
		figure.update_layout(
			title={
				'text': self.__class__.__name__,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			showlegend=True)
		y_title = [string for string in Metrics.get_all_metric_docs() if y_name.upper() in string][0]
		figure.update_yaxes(
      		title=y_title)
		return figure
# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(MerByModelnameByDataset)

class WilByModelnameByDataset(BasePlotly):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
   
		y_name = "wil"

		chart_data = pd.concat([
			df['model_name'],
			df[y_name],
			df['dataset'],
		], axis=1)

		figure = px.box(chart_data, x="model_name", y=y_name, color="dataset")
		for s in df["model_name"].unique():
			figure.add_annotation(x=s,
							y = df[df['model_name']==s][y_name].max(),
							text = f"{len(df[df['model_name']==s]['model_name'])}",
							yshift = 10,
							showarrow = False
							)
		figure.update_layout(
			title={
				'text': self.__class__.__name__,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			showlegend=True)
		y_title = [string for string in Metrics.get_all_metric_docs() if y_name.upper() in string][0]
		figure.update_yaxes(
      		title=y_title)
		return figure
# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(WilByModelnameByDataset)

class WipByModelnameByDataset(BasePlotly):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
   
		y_name = "wip"

		chart_data = pd.concat([
			df['model_name'],
			df[y_name],
			df['dataset'],
		], axis=1)

		figure = px.box(chart_data, x="model_name", y=y_name, color="dataset")
		for s in df["model_name"].unique():
			figure.add_annotation(x=s,
							y = df[df['model_name']==s][y_name].max(),
							text = f"{len(df[df['model_name']==s]['model_name'])}",
							yshift = 10,
							showarrow = False
							)
		figure.update_layout(
			title={
				'text': self.__class__.__name__,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			showlegend=True)
		y_title = [string for string in Metrics.get_all_metric_docs() if y_name.upper() in string][0]
		figure.update_yaxes(
      		title=y_title)
		return figure
# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(WipByModelnameByDataset)

class PlotGenDynamically(DynamicallyCreatePlotClassesByMetricByDatabase):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		# dataset_name = self.get_dataset_name()
		y_name = self.metric_name
		y_title = self.metric_description
  
		x_name = "model_name"
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
		df = df.query(f'dataset=="{self.dataset_name}"')
		
		chart_data = pd.concat([
			df[x_name],
			df[y_name],
			# df['dataset'],
		], axis=1)

		# figure = px.box(chart_data, x=x_name, y=y_name, color="dataset")
		figure = px.box(chart_data, x=x_name, y=y_name)
		for s in df[x_name].unique():
			figure.add_annotation(x=s,
							y = df[df[x_name]==s][y_name].max(),
							text = f"{len(df[df[x_name]==s][x_name])}",
							yshift = 10,
							showarrow = False
							)
		figure.update_layout(
			title={
				'text': self.__class__.__name__,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'},
			showlegend=True)

		figure.update_yaxes(
      		title=y_title)
		return figure
# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(PlotGenDynamically)