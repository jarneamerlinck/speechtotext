#!/usr/bin/env python
import threading
import os
import re
import torch

REGEX_STRING_PARSE = '[^A-Za-z0-9 ]+'

def force_cudnn_initialization():
	"""Force cuda use for torch.
	"""    
	s = 32
	dev = torch.device('cuda')
	torch.nn.functional.conv2d(torch.zeros(s, s, s, s, device=dev), torch.zeros(s, s, s, s, device=dev))

def string_cleaning(text:str)-> str:
	"""Cleaning of string for STT.

	Args:
		text (str): uncleaned string.

	Returns:
		str: cleaned string.
	"""    
	return re.sub(REGEX_STRING_PARSE, '', text)






