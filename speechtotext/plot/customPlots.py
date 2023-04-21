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
class MeanOfMetricByModelname(BasePlotly):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)

		df = df.reset_index().drop('index', axis=1, errors='ignore')
		df.columns = [str(c) for c in df.columns]  # update columns to strings in case they are numbers

		chart_data = pd.concat([
			df['model_name'],
			df['wer'],
			df['mer'],
			df['wil'],
			df['wip'],
			df['cer'],
		], axis=1)
		chart_data = chart_data.sort_values(['model_name'])
		chart_data = chart_data.rename(columns={'model_name': 'x'})
		chart_data_mean = chart_data.groupby(['x'], dropna=True)[['wer', 'mer', 'wil', 'wip', 'cer']].mean()
		chart_data_mean.columns = ['wer|mean','mer|mean','wil|mean','wip|mean','cer|mean']
		chart_data = chart_data_mean.reset_index()
		chart_data = chart_data.dropna()

		charts = []
		charts.append(go.Bar(
			x=chart_data['x'],
			y=chart_data['wer|mean'],
			name='Mean of wer'
		))
		charts.append(go.Bar(
			x=chart_data['x'],
			y=chart_data['mer|mean'],
			name='Mean of mer'
		))
		charts.append(go.Bar(
			x=chart_data['x'],
			y=chart_data['wil|mean'],
			name='Mean of wil'
		))
		charts.append(go.Bar(
			x=chart_data['x'],
			y=chart_data['wip|mean'],
			name='Mean of wip'
		))
		charts.append(go.Bar(
			x=chart_data['x'],
			y=chart_data['cer|mean'],
			name='Mean of cer'
		))
		figure = go.Figure(data=charts, layout=go.Layout({
			'barmode': 'group',
			'legend': {'orientation': 'h', 'y': -0.3},
			'title': {'text': 'Mean of wer, Mean of mer, Mean of wil, Mean of wip, Mean of cer by model_name'},
			'xaxis': {'title': {'text': 'model_name'}},
			'yaxis': {'title': {'text': 'Mean of wer, Mean of mer, Mean of wil, Mean of wip, Mean of cer'}, 'type': 'linear'}
		}))
		return figure
# Add model to Plotting
Plotting.CUSTOM_PLOTS.append(MeanOfMetricByModelname)

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