#!/usr/bin/env python
import threading
import os
import re
import torch
import functools
import pandas as pd

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



def multidispatch(*types):
	"""Allow for Method overloading.
	"""    
	def register(function):
		name = function.__name__
		mm = multidispatch.registry.get(name)
		if mm is None:
			@functools.wraps(function)
			def wrapper(self, *args):
				types = tuple(arg.__class__ for arg in args) 
				function = wrapper.typemap.get(types)
				if function is None:
					raise TypeError("no match")
				return function(self, *args)
			wrapper.typemap = {}
			mm = multidispatch.registry[name] = wrapper
		if types in mm.typemap:
			raise TypeError("duplicate registration")
		mm.typemap[types] = function
		return mm
	return register
multidispatch.registry = {}