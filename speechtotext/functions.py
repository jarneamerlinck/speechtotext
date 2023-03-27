#!/usr/bin/env python
import threading
import os
import re

REGEX_STRING_PARSE = '[^A-Za-z0-9 ]+'

def string_cleaning(text:str)-> str:
	"""Cleaning of string for STT

	Args:
		text (str): uncleaned string

	Returns:
		str: cleaned string
	"""    
	return re.sub(REGEX_STRING_PARSE, '', text)






