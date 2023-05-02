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
from jiwer import cer, process_words
import pandas as pd
from docstring_parser import parse

import nltk
from nltk import word_tokenize
from nltk.translate.bleu_score import sentence_bleu,SmoothingFunction
from nltk.translate.meteor_score import meteor_score
from rouge import Rouge

from speechtotext.datasets import Dataset
from speechtotext.functions import string_cleaning 

class Metrics():
	"""Class to calulate the metrics.
	
	Attributes:
		wer (float): Word error rate (WER).

			The WER is how many words there were made errors on.
		mer (float): Match error rate (MER).
  
			The MER indicates the percentage of words that were incorrectly predicted and inserted. 
		wil (float): Word information lost (WIL).
  
			The WIL represents the word information that is lost.
		wip (float): Word information preserved (WIP).
  
			The WIP represents the word information that is preserved.
		cer (float): Character error rate (CER).
  
			The CER is how many characters there were made errors on.
		substitutions (int): Number of words substituted (substitutions).
  
			The substitutions is the number of words that were replaced.
		insertions (int): Number of words inserted (insertions).
  
			The insertions is the number of words that were added.
		deletions (int): Number of words deleted (deletions).

			The deletions is the number of words that were removed.
		duration (float): Duration of the transcribing (duration).

			The duration is how long it took to transcribe the audiofile.
		meteor (float): Metric for Evaluation of Translation with Explicit ORdering (METEOR).

			METEOR is an automatic metric for machine translation evaluation that is based on a generalized concept of
			unigram matching between the machine-produced translation and human-produced reference translations.
		blue (float): Bilingual Evaluation Understudy (BLUE).

			BLUE is used in comparing a candidate translation to one or more reference translations.
 		rouge_1_r (float): Recall-Oriented Understudy for Gisting Evaluation recall of 1-grams (ROUGE-1-r).

			ROUGE includes measures to automatically determine the quality of a summary 
   			by comparing it to other (ideal) summaries created by humans.
			ROUGE-1-r is the recall of 1-grams.
		rouge_1_p (float): Recall-Oriented Understudy for Gisting Evaluation precision of 1-grams (ROUGE-1-p).

			ROUGE includes measures to automatically determine the quality of a summary 
   			by comparing it to other (ideal) summaries created by humans.
			ROUGE-1-p is the precision of 1-grams.
		rouge_1_f (float): Recall-Oriented Understudy for Gisting Evaluation F1-score of 1-grams (ROUGE-1-f).

			ROUGE includes measures to automatically determine the quality of a summary 
   			by comparing it to other (ideal) summaries created by humans.
			ROUGE-1-f is the F1-score of 1-grams.
		rouge_2_r (float): Recall-Oriented Understudy for Gisting Evaluation recall of 2-grams (ROUGE-2-r).

			ROUGE includes measures to automatically determine the quality of a summary 
   			by comparing it to other (ideal) summaries created by humans.
			ROUGE-2-r is the recall of 2-grams.
		rouge_2_p (float): Recall-Oriented Understudy for Gisting Evaluation precision of 2-grams (ROUGE-2-p).

			ROUGE includes measures to automatically determine the quality of a summary 
   			by comparing it to other (ideal) summaries created by humans.
			ROUGE-2-p is the precision of 2-grams.
		rouge_2_f (float): Recall-Oriented Understudy for Gisting Evaluation F1-score of 2-grams (ROUGE-2-f).

			ROUGE includes measures to automatically determine the quality of a summary 
   			by comparing it to other (ideal) summaries created by humans.
			ROUGE-2-f is the F1-score of 2-grams.  
		rouge_l_r (float): Recall-Oriented Understudy for Gisting Evaluation recall of LCS (ROUGE-L-r).

			ROUGE-L is based on the longest common subsequence (LCS) between our model output and reference.
			ROUGE-L-r is the recall of LCS.
		rouge_l_p (float): Recall-Oriented Understudy for Gisting Evaluation precision of LCS (ROUGE-L-p).

			ROUGE-L is based on the longest common subsequence (LCS) between our model output and reference.
			ROUGE-l-p is the precision of LCS.
		rouge_l_f (float): Recall-Oriented Understudy for Gisting Evaluation F1-score of LCS (ROUGE-L-f).

			ROUGE-L is based on the longest common subsequence (LCS) between our model output and reference.
			ROUGE-L-f is the F1-score of LCS.
   
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
		# Order here is used in the outputs
		result = process_words(self.reference, self.hypothesis)
		self.wer = result.wer
		self.mer = result.mer
		self.wil = result.wil
		self.wip = result.wip
		self.cer = cer(self.reference, self.hypothesis)
		self.insertions = result.insertions
		self.deletions = result.deletions
		self.substitutions = result.substitutions

		self.meteor = meteor_score(references=[word_tokenize(self.reference)],
                             hypothesis=word_tokenize(self.hypothesis))

		rouge_scores = Rouge().get_scores(hyps=self.hypothesis, refs=self.reference, avg=True)
		[setattr(self, f"{rouge_type}-{metric}".replace("-", "_"), rouge_scores[rouge_type][metric]) for rouge_type in rouge_scores.keys() for metric in rouge_scores[rouge_type].keys()]
		self.blue = sentence_bleu(references=[word_tokenize(self.reference)],
                             hypothesis=word_tokenize(self.hypothesis),
                             smoothing_function=SmoothingFunction().method4)

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
			to_add = str(param.description)[:-1]
			to_add = to_add[:to_add.find(')')+1]
			list_of_metrics_docs.append(to_add)
   


		def prepare_for_sorting(s:str):
			start = '('
			end = ')'
			return ((s.split(start))[1].split(end)[0]).lower().replace("-", "_")

		order = {value:index for index,value in enumerate(Metrics.get_all_metric_names())}
		return sorted(list_of_metrics_docs, key=lambda x: order[prepare_for_sorting(x)])

	@override
	def __str__(self) -> str:
		return f"wer: {self.wer}, mer: {self.mer}, wil: {self.wil}, wip: {self.wip}, cer: {self.cer}"
	
