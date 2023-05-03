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

from speechtotext.plot.plotting import  Plotting, DynamicPlotClassesByMetricByDataset, DynamicPlotClassesByMetricForEachDataset

class DynamicallyByModelNameForEachDataset(DynamicPlotClassesByMetricForEachDataset):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		y_name = self.metric_name
		y_title = self.metric_description
  
		x_name = "model_name"
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
		df = df.query(f'dataset=="{self.dataset_name}"')
		
		chart_data = pd.concat([
			df[x_name],
			df[y_name]
		], axis=1)

		fig_width= 300+ 75* df[x_name].nunique()
		figure = px.box(chart_data, x=x_name, y=y_name, width=fig_width)
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
Plotting.CUSTOM_PLOTS.append(DynamicallyByModelNameForEachDataset)

class DynamicallyByModelNameByDataset(DynamicPlotClassesByMetricByDataset):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		y_name = self.metric_name
		y_title = self.metric_description
		x_name = "model_name"
		group_name = "dataset"

		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)
   

		chart_data = pd.concat([
			df[x_name],
			df[y_name],
			df[group_name],
		], axis=1)

		fig_width= 300+ 75* df[x_name].nunique() +  (df[x_name].nunique()*df[group_name].nunique()* 5)
		figure = px.box(chart_data, x=x_name, y=y_name, color=group_name, width=fig_width)
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
Plotting.CUSTOM_PLOTS.append(DynamicallyByModelNameByDataset)