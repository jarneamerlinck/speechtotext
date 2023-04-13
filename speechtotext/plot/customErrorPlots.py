"""Module to create custom error plots for the plotting module

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
	Plotting.CUSTOM_ERRORS.append(BoxPlotOfModelsWer)

	# Create class with plotly picture
	from speechtotext.plot.plotting import BasePlot, Plotting
	class DemoPlotlyExample(BasePlot):

		def create_plot(self) -> plotly.graph_objs._figure.Figure:
			self.df = px.data.gapminder().query("country=='Canada'")
			fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
			return fig

	# Add model to Plotting
	Plotting.CUSTOM_ERRORS.append(DemoPlotlyExample)
"""
import plotly
import plotly.express as px
import plotly.tools as tls
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import matplotlib

from speechtotext.plot.plotting import BasePlotly, Plotting, BaseMatPlotLib

class ErrorCountByModel(BasePlotly):
	"""Class that is used to create error plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:
		df = self.df
		y_name = 'audio_ID'
		if isinstance(df, (pd.DatetimeIndex, pd.MultiIndex)):
			df = df.to_frame(index=False)

		df = df.reset_index().drop('index', axis=1, errors='ignore')
		df.columns = [str(c) for c in df.columns]

		chart_data = pd.concat([
			df['model_name'],
			df[y_name],
		], axis=1)
		chart_data = chart_data.sort_values(['model_name'])
		chart_data = chart_data.rename(columns={'model_name': 'x'})
		chart_data_count = chart_data.groupby(['x'], dropna=True)[[y_name]].count()
		chart_data_count.columns = [f'{y_name}|count']
		chart_data = chart_data_count.reset_index()
		chart_data = chart_data.dropna()

		charts = []
		charts.append(go.Bar(
			x=chart_data['x'],
			y=chart_data[f'{y_name}|count']
		))
		figure = go.Figure(data=charts, layout=go.Layout({
			'barmode': 'group',
			'legend': {'orientation': 'h', 'y': -0.3},
			'title': {'text': 'Count of errors by model_name'},
			'xaxis': {'title': {'text': 'model_name'}},
			'yaxis': {'tickformat': '0:g', 'title': {'text': 'Count of errors'}, 'type': 'linear'}
		}))
		for s in df["model_name"].unique():
							figure.add_annotation(x=s,
											y = df[df['model_name']==s][y_name].count(),
											text = f"{len(df[df['model_name']==s]['model_name'])}",
											yshift = 10,
											showarrow = False
											)
		figure.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
		return figure
# Add model to Plotting
Plotting.CUSTOM_ERROR_PLOTS.append(ErrorCountByModel)

class ErrorCountByModelByDataset(BasePlotly):
	"""Class that is used to create error plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:
		df = self.df
		y_name = 'audio_ID'
		group_name = 'dataset'
		x_name = 'model_name'

		chart_data = pd.concat([
					df['model_name'],
					df[y_name],
					df['dataset'],
				], axis=1)

		chart_data_count = chart_data.groupby(['dataset',x_name], dropna=True)[['audio_ID']].count()
		chart_data_count.columns = ['audio_ID|count']
		chart_data = chart_data_count.reset_index()
		chart_data = chart_data.dropna()
		figure = px.bar(chart_data, x=x_name, y=f"{y_name}|count", color="dataset", barmode="group")

		figure.update_layout(
			barmode= 'group',
			legend= {'orientation': 'h', 'y': -0.3},
			title= {'text': 'Count of errors by model_name', 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'},
			xaxis= {'title': {'text': 'model_name'}},
			yaxis= {'tickformat': '0:g', 'title': {'text': 'Count of errors'}, 'type': 'linear'},
			showlegend=True)
		return figure
# Add model to Plotting
Plotting.CUSTOM_ERROR_PLOTS.append(ErrorCountByModelByDataset)

class ErrorCountHeatmap(BasePlotly):
	"""Class that is used to create error plots for an benchmark.
	"""    
	def create_plot(self) -> plotly.graph_objs._figure.Figure:
		df = self.df
		count_data = df.groupby(['model_name','dataset'], sort=False).size().reset_index(name='count')
		count_data = count_data.set_index(['model_name','dataset'])
		data = count_data.unstack(0).T
		data



		x_name = "dataset"
		y_name = "model_name"
		figure = go.Figure(data=go.Heatmap(
					z=data.T,
					x=data.index.get_level_values(y_name),
					y=data.columns,
					hoverongaps = False,
     				colorscale=plotly.colors.sequential.Blackbody_r),
					layout=go.Layout({
						'barmode': 'group',
						'legend': {'orientation': 'h', 'y': -0.3},
						'title': {'text': 'Heatmap of error count by model_name by dataset'},
						'xaxis': {'title': {'text': 'dataset'}},
						'yaxis': {'tickformat': '0:g', 'title': {'text': 'model_name'}}
					})
     	)
		return figure
# Add model to Plotting
Plotting.CUSTOM_ERROR_PLOTS.append(ErrorCountHeatmap)
