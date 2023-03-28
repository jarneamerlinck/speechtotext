#!/usr/bin/env python
import threading
import os
import re
from speechtotext.datasets import Dataset
from typing_extensions import override
from jiwer import wer, mer, wil, wip, cer

from speechtotext.functions import string_cleaning 

def notebook_metrics_print(dataset:Dataset, id:str, hypothesis:str):
	"""Print metrics from transcript and hypothesis.

	Args:
		dataset (Dataset): dataset of audio.
		id (str): id of the audio file.
		hypothesis (str): hypothesis transcript.
	"""    
	reference = dataset.get_text_of_id(id)
	m = Metrics(reference,hypothesis, id)
	print(f"reference: {m.reference}")
	print(f"hypothesis: {m.hypothesis}")
	print(m)

class Metrics():
	"""Class to calulate the metrics.
	Attributes:
		class_attribute (str): (class attribute) The class attribute.
		wer (float): (class attribute) word error rate (WER).
		mer (float): (class attribute) match error rate (MER).
		wil (float): (class attribute) word information lost (WIL).
		wip (float): (class attribute) word information preserved (WIP).
		cer (float): (class attribute) character error rate (CER).
		
	"""    

	def __init__(self, reference:str, hypothesis:str, audio_id:str, with_cleaning=True):
	
		"""Class to calulate the metrics.

		Args:
			reference (str): reference transcript.
			hypothesis (str): hypothesis transcript.
   			audio_id (str): id of the audio file.
			with_cleaning (bool, optional): Set True to clean transcripts. Defaults to True.
		"""     
		if with_cleaning:
			reference = string_cleaning(reference)
			hypothesis = string_cleaning(hypothesis)

		self.reference = reference
		self.hypothesis = hypothesis
		self.audio_id = audio_id
		self()

	def __call__(self, *args, **kwds):
		"""Calculate the metrics.
		"""     
		self.wer = wer(self.reference, self.hypothesis)
		self.mer = mer(self.reference, self.hypothesis)
		self.wil = wil(self.reference, self.hypothesis)
		self.wip = wip(self.reference, self.hypothesis)
		self.cer = cer(self.reference, self.hypothesis)

	@override
	def __str__(self) -> str:
		return f"wer: {self.wer}, mer: {self.mer}, wil: {self.wil}, wip: {self.wip}, cer: {self.cer}"





