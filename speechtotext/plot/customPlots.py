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
	Plotting.CUSTOM_RESULTS.append(BoxPlotOfModelsWer)

	# Create class with plotly picture
	from speechtotext.plot.plotting import BasePlot, Plotting
	class DemoPlotlyExample(BasePlot):

		def create_plot(self) -> plotly.graph_objs._figure.Figure:
			self.df = px.data.gapminder().query("country=='Canada'")
			fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
			return fig

	# Add model to Plotting
	Plotting.CUSTOM_RESULTS.append(DemoPlotlyExample)
"""
import plotly
import plotly.express as px
import plotly.tools as tls
import pandas as pd
import seaborn as sns
import matplotlib

from speechtotext.plot.plotting import BasePlotly, Plotting, BaseMatPlotLib

class MeanOfMetricByModelname(BasePlotly):
	"""Class that is used to create plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:

		df = self.df
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)

		# remove any pre-existing indices for ease of use in the D-Tale code, but this is not required
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

		import plotly.graph_objs as go

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
Plotting.CUSTOM_RESULTS.append(MeanOfMetricByModelname)

class BoxPlotOfModelsWer(BaseMatPlotLib):
	"""Class that is used to create boxplot for wer by models.
	"""    
	def create_plot(self) -> matplotlib.figure.Figure:
		plot = sns.boxplot(data=self.df, x="wer", y="model_name")
		fig = plot.get_figure()
		return fig
# Add models to Plotting
Plotting.CUSTOM_RESULTS.append(BoxPlotOfModelsWer)

class BoxPlotOfModelsMer(BaseMatPlotLib):
	"""Class that is used to create boxplot for mer by models.
	"""    
	def create_plot(self) -> matplotlib.figure.Figure:
		plot = sns.boxplot(data=self.df, x="mer", y="model_name")
		fig = plot.get_figure()
		return fig
# Add models to Plotting
Plotting.CUSTOM_RESULTS.append(BoxPlotOfModelsMer)

class BoxPlotOfModelsWil(BaseMatPlotLib):
	"""Class that is used to create boxplot for wil by models.
	"""    
	def create_plot(self) -> matplotlib.figure.Figure:
		plot = sns.boxplot(data=self.df, x="wil", y="model_name")
		fig = plot.get_figure()
		return fig
# Add models to Plotting
Plotting.CUSTOM_RESULTS.append(BoxPlotOfModelsWil)

class BoxPlotOfModelsWip(BaseMatPlotLib):
	"""Class that is used to create boxplot for wip by models.
	"""    
	def create_plot(self) -> matplotlib.figure.Figure:
		plot = sns.boxplot(data=self.df, x="wip", y="model_name")
		fig = plot.get_figure()
		return fig
# Add models to Plotting
Plotting.CUSTOM_RESULTS.append(BoxPlotOfModelsWip)

class BoxPlotOfModelsCer(BaseMatPlotLib):
	"""Class that is used to create boxplot for cer by models.
	"""    
	def create_plot(self) -> matplotlib.figure.Figure:
		plot = sns.boxplot(data=self.df, x="cer", y="model_name")
		fig = plot.get_figure()
		return fig
# Add models to Plotting
Plotting.CUSTOM_RESULTS.append(BoxPlotOfModelsCer)