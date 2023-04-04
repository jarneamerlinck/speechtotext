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
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import matplotlib

from speechtotext.plot.plotting import BasePlotly, Plotting, BaseMatPlotLib

class MeanOfMerByModelnameByDataset(BasePlotly):
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
			df['mer'],
			df['dataset'],
		], axis=1)
		chart_data = chart_data.query("""(`dataset` == '20000_mijlen') or (`dataset` == 'RDH_VL')""")
		s = chart_data['model_name']
		chart_data.loc[:, 'model_name'] = s
		s = chart_data['dataset']
		chart_data.loc[:, 'dataset'] = s
		chart_data = chart_data.sort_values(['dataset', 'model_name'])
		chart_data = chart_data.rename(columns={'model_name': 'x'})
		chart_data_mean = chart_data.groupby(['dataset','x'], dropna=True)[['mer']].mean()
		chart_data_mean.columns = ['mer|mean']
		chart_data = chart_data_mean.reset_index()
		chart_data = chart_data.dropna()

		charts = []
		chart_data_20000 = chart_data.query("""`dataset` == '20000_mijlen'""")
		chart_data_RDH_VL = chart_data.query("""`dataset` == 'RDH_VL'""")
		charts.append(go.Bar(
			x=chart_data_20000['x'],
			y=chart_data_20000['mer|mean'],
			name='(dataset: 20000_mijlen)'
		))
		charts.append(go.Bar(
			x=chart_data_RDH_VL['x'],
			y=chart_data_RDH_VL['mer|mean'],
			name='(dataset: RDH_VL)'
		))
		figure = go.Figure(data=charts, layout=go.Layout({
			'barmode': 'group',
			'legend': {'orientation': 'h', 'y': -0.3},
			'title': {'text': 'Mean of mer by model_name'},
			'xaxis': {'title': {'text': 'model_name'}},
			'yaxis': {'title': {'text': 'Mean of mer'}, 'type': 'linear'}
		}))
		return figure
Plotting.CUSTOM_RESULTS.append(MeanOfMerByModelnameByDataset)

class MeanOfWerByModelnameByDataset(BasePlotly):
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
			df['dataset'],
		], axis=1)
		chart_data = chart_data.query("""(`dataset` == '20000_mijlen') or (`dataset` == 'RDH_VL')""")
		s = chart_data['model_name']
		chart_data.loc[:, 'model_name'] = s
		s = chart_data['dataset']
		chart_data.loc[:, 'dataset'] = s
		chart_data = chart_data.sort_values(['dataset', 'model_name'])
		chart_data = chart_data.rename(columns={'model_name': 'x'})
		chart_data_mean = chart_data.groupby(['dataset','x'], dropna=True)[['wer']].mean()
		chart_data_mean.columns = ['wer|mean']
		chart_data = chart_data_mean.reset_index()
		chart_data = chart_data.dropna()

		charts = []
		chart_data_20000 = chart_data.query("""`dataset` == '20000_mijlen'""")
		chart_data_RDH_VL = chart_data.query("""`dataset` == 'RDH_VL'""")
		charts.append(go.Bar(
			x=chart_data_20000['x'],
			y=chart_data_20000['wer|mean'],
			name='(dataset: 20000_mijlen)'
		))
		charts.append(go.Bar(
			x=chart_data_RDH_VL['x'],
			y=chart_data_RDH_VL['wer|mean'],
			name='(dataset: RDH_VL)'
		))
		figure = go.Figure(data=charts, layout=go.Layout({
			'barmode': 'group',
			'legend': {'orientation': 'h', 'y': -0.3},
			'title': {'text': 'Mean of wer by model_name'},
			'xaxis': {'title': {'text': 'model_name'}},
			'yaxis': {'title': {'text': 'Mean of wer'}, 'type': 'linear'}
		}))
		return figure
# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(MeanOfWerByModelnameByDataset)

class MeanOfWilByModelnameByDataset(BasePlotly):
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
			df['wil'],
			df['dataset'],
		], axis=1)
		chart_data = chart_data.query("""(`dataset` == '20000_mijlen') or (`dataset` == 'RDH_VL')""")
		s = chart_data['model_name']
		chart_data.loc[:, 'model_name'] = s
		s = chart_data['dataset']
		chart_data.loc[:, 'dataset'] = s
		chart_data = chart_data.sort_values(['dataset', 'model_name'])
		chart_data = chart_data.rename(columns={'model_name': 'x'})
		chart_data_mean = chart_data.groupby(['dataset','x'], dropna=True)[['wil']].mean()
		chart_data_mean.columns = ['wil|mean']
		chart_data = chart_data_mean.reset_index()
		chart_data = chart_data.dropna()

		charts = []
		chart_data_20000 = chart_data.query("""`dataset` == '20000_mijlen'""")
		chart_data_RDH_VL = chart_data.query("""`dataset` == 'RDH_VL'""")
		charts.append(go.Bar(
			x=chart_data_20000['x'],
			y=chart_data_20000['wil|mean'],
			name='(dataset: 20000_mijlen)'
		))
		charts.append(go.Bar(
			x=chart_data_RDH_VL['x'],
			y=chart_data_RDH_VL['wil|mean'],
			name='(dataset: RDH_VL)'
		))
		figure = go.Figure(data=charts, layout=go.Layout({
			'barmode': 'group',
			'legend': {'orientation': 'h', 'y': -0.3},
			'title': {'text': 'Mean of wil by model_name'},
			'xaxis': {'title': {'text': 'model_name'}},
			'yaxis': {'title': {'text': 'Mean of wil'}, 'type': 'linear'}
		}))
		return figure
# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(MeanOfWilByModelnameByDataset)

class MeanOfCerByModelnameByDataset(BasePlotly):
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
			df['cer'],
			df['dataset'],
		], axis=1)
		chart_data = chart_data.query("""(`dataset` == '20000_mijlen') or (`dataset` == 'RDH_VL')""")
		s = chart_data['model_name']
		chart_data.loc[:, 'model_name'] = s
		s = chart_data['dataset']
		chart_data.loc[:, 'dataset'] = s
		chart_data = chart_data.sort_values(['dataset', 'model_name'])
		chart_data = chart_data.rename(columns={'model_name': 'x'})
		chart_data_mean = chart_data.groupby(['dataset','x'], dropna=True)[['cer']].mean()
		chart_data_mean.columns = ['cer|mean']
		chart_data = chart_data_mean.reset_index()
		chart_data = chart_data.dropna()

		charts = []
		chart_data_20000 = chart_data.query("""`dataset` == '20000_mijlen'""")
		chart_data_RDH_VL = chart_data.query("""`dataset` == 'RDH_VL'""")
		charts.append(go.Bar(
			x=chart_data_20000['x'],
			y=chart_data_20000['cer|mean'],
			name='(dataset: 20000_mijlen)'
		))
		charts.append(go.Bar(
			x=chart_data_RDH_VL['x'],
			y=chart_data_RDH_VL['cer|mean'],
			name='(dataset: RDH_VL)'
		))
		figure = go.Figure(data=charts, layout=go.Layout({
			'barmode': 'group',
			'legend': {'orientation': 'h', 'y': -0.3},
			'title': {'text': 'Mean of cer by model_name'},
			'xaxis': {'title': {'text': 'model_name'}},
			'yaxis': {'title': {'text': 'Mean of cer'}, 'type': 'linear'}
		}))
		return figure
# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(MeanOfCerByModelnameByDataset)

class MeanOfWipByModelnameByDataset(BasePlotly):
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
			df['wip'],
			df['dataset'],
		], axis=1)
		chart_data = chart_data.query("""(`dataset` == '20000_mijlen') or (`dataset` == 'RDH_VL')""")
		s = chart_data['model_name']
		chart_data.loc[:, 'model_name'] = s
		s = chart_data['dataset']
		chart_data.loc[:, 'dataset'] = s
		chart_data = chart_data.sort_values(['dataset', 'model_name'])
		chart_data = chart_data.rename(columns={'model_name': 'x'})
		chart_data_mean = chart_data.groupby(['dataset','x'], dropna=True)[['wip']].mean()
		chart_data_mean.columns = ['wip|mean']
		chart_data = chart_data_mean.reset_index()
		chart_data = chart_data.dropna()

		charts = []
		chart_data_20000 = chart_data.query("""`dataset` == '20000_mijlen'""")
		chart_data_RDH_VL = chart_data.query("""`dataset` == 'RDH_VL'""")
		charts.append(go.Bar(
			x=chart_data_20000['x'],
			y=chart_data_20000['wip|mean'],
			name='(dataset: 20000_mijlen)'
		))
		charts.append(go.Bar(
			x=chart_data_RDH_VL['x'],
			y=chart_data_RDH_VL['wip|mean'],
			name='(dataset: RDH_VL)'
		))
		figure = go.Figure(data=charts, layout=go.Layout({
			'barmode': 'group',
			'legend': {'orientation': 'h', 'y': -0.3},
			'title': {'text': 'Mean of wip by model_name'},
			'xaxis': {'title': {'text': 'model_name'}},
			'yaxis': {'title': {'text': 'Mean of wip'}, 'type': 'linear'}
		}))
		return figure
# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(MeanOfWipByModelnameByDataset)

class MeanOfMerByModelnameByDataset(BasePlotly):
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
			df['mer'],
			df['dataset'],
		], axis=1)
		chart_data = chart_data.query("""(`dataset` == '20000_mijlen') or (`dataset` == 'RDH_VL')""")
		s = chart_data['model_name']
		chart_data.loc[:, 'model_name'] = s
		s = chart_data['dataset']
		chart_data.loc[:, 'dataset'] = s
		chart_data = chart_data.sort_values(['dataset', 'model_name'])
		chart_data = chart_data.rename(columns={'model_name': 'x'})
		chart_data_mean = chart_data.groupby(['dataset','x'], dropna=True)[['mer']].mean()
		chart_data_mean.columns = ['mer|mean']
		chart_data = chart_data_mean.reset_index()
		chart_data = chart_data.dropna()

		charts = []
		chart_data_20000 = chart_data.query("""`dataset` == '20000_mijlen'""")
		chart_data_RDH_VL = chart_data.query("""`dataset` == 'RDH_VL'""")
		charts.append(go.Bar(
			x=chart_data_20000['x'],
			y=chart_data_20000['mer|mean'],
			name='(dataset: 20000_mijlen)'
		))
		charts.append(go.Bar(
			x=chart_data_RDH_VL['x'],
			y=chart_data_RDH_VL['mer|mean'],
			name='(dataset: RDH_VL)'
		))
		figure = go.Figure(data=charts, layout=go.Layout({
			'barmode': 'group',
			'legend': {'orientation': 'h', 'y': -0.3},
			'title': {'text': 'Mean of mer by model_name'},
			'xaxis': {'title': {'text': 'model_name'}},
			'yaxis': {'title': {'text': 'Mean of mer'}, 'type': 'linear'}
		}))
		return figure
# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(MeanOfMerByModelnameByDataset)

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