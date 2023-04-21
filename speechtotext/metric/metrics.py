"""Module that calculates the metrics for speechtotext models.

Use this module like this:
	
.. code-block:: python

	# Imports
	from speechtotext.metric.metrics import Metrics
	
	# Create metrics
	m = Metrics("De stoel heeft krassen gemaakt op de vloer!", "De stoel heeft krassen gemaakt op de vloer", "id_from_dataset", duration=0.5)
	print(m)
"""
from typing_extensions import override
from jiwer import wer, mer, wil, wip, cer 
import pandas as pd
from docstring_parser import parse

from speechtotext.datasets import Dataset
from speechtotext.functions import string_cleaning 

def notebook_metrics_print(dataset:Dataset, id:str, hypothesis:str):
	"""Print metrics from transcript and hypothesis.

	Args:
		dataset (Dataset): Dataset of audio.
		id (str): Id of the audio file.
		hypothesis (str): Hypothesis transcript.
	"""    
	reference = dataset.get_text_of_id(id)
	m = Metrics(reference,hypothesis, id, duration=0)
	print(f"reference: {m.reference}")
	print(f"hypothesis: {m.hypothesis}")
	print(m)

class Metrics():
	"""Class to calulate the metrics.
	
	Attributes:
		wer (float): Word error rate (WER).
		mer (float): Match error rate (MER).
		wil (float): Word information lost (WIL).
		wip (float): Word information preserved (WIP).
		cer (float): Character error rate (CER).
		duration (float): Duration of the transcribing (duration).
		
	"""    

	def __init__(self, reference:str, hypothesis:str, audio_id:str, duration:float, with_cleaning=True):
	
		"""Class to calulate the metrics.

		Args:
			reference (str): Reference transcript.
			hypothesis (str): Hypothesis transcript.
   			audio_id (str): Id of the audio file.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.
		"""     
		if with_cleaning:
			reference = string_cleaning(reference)
			hypothesis = string_cleaning(hypothesis)

		self.reference = reference
		self.hypothesis = hypothesis
		self.audio_id = audio_id
		self.duration = duration
		self()

	def __call__(self, *args, **kwds):
		"""Calculate the metrics.
		"""     
		self.wer = wer(self.reference, self.hypothesis)
		self.mer = mer(self.reference, self.hypothesis)
		self.wil = wil(self.reference, self.hypothesis)
		self.wip = wip(self.reference, self.hypothesis)
		self.cer = cer(self.reference, self.hypothesis)

	def get_all_metric_names() -> list[str]:
		"""Returns all possible metric names in a list. 

		Returns:
			list[str]: List of all metric names.
		"""     
		m  = Metrics(reference= "reference", hypothesis= "hypothesis", audio_id= "audio_id", duration=2, with_cleaning=False)
		list_of_metrics = list(vars(m).keys())
		# Only keep metrics
		list_of_metrics.remove("reference")
		list_of_metrics.remove("hypothesis")
		list_of_metrics.remove("audio_id")

		return list_of_metrics

	def get_all_metric_docs() -> list[str]:
		"""Returns all descriptions of metrics returned by get_all_metric_names in the correct order.

		Returns:
			list[str]: List of all metric descriptions.
		"""     
		m  = Metrics(reference= "reference", hypothesis= "hypothesis", audio_id= "audio_id", duration=2, with_cleaning=False)
		docstring = parse(m.__doc__)
		list_of_metrics_docs = []
		for param in docstring.params:
			list_of_metrics_docs.append(str(param.description)[:-1])
   


		def prepare_for_sorting(s):
			start = '('
			end = ')'
			return ((s.split(start))[1].split(end)[0]).lower()

		order = {v:i for i,v in enumerate(Metrics.get_all_metric_names())}
		return sorted(list_of_metrics_docs, key=lambda x: order[prepare_for_sorting(x)])


	@override
	def __str__(self) -> str:
		return f"wer: {self.wer}, mer: {self.mer}, wil: {self.wil}, wip: {self.wip}, cer: {self.cer}"
	

