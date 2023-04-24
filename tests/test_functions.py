import pytest

def test_module_import():
	"""Test base import.
	"""    
	import speechtotext.functions
def test_string_cleaning_same():
	"""Test string_cleaning.
	"""  
	from speechtotext.functions import string_cleaning
	original_string:str = "This needs to be cleaned"
	cleaned_string:str = "This needs to be cleaned"
	assert cleaned_string == string_cleaning(original_string)
def test_string_cleaning_diff():
	"""Test string_cleaning.
	"""  
	from speechtotext.functions import string_cleaning
	original_string:str = "This needs to be cleanedd"
	cleaned_string:str = "This needs to be cleaned"
	assert cleaned_string != string_cleaning(original_string)

def test_string_cleaning_diff_number():
	"""Test string_cleaning.
	"""  
	from speechtotext.functions import string_cleaning
	original_string:str = "This needs to 3be cleaned"
	cleaned_string:str = "This needs to be cleaned"
	assert cleaned_string != string_cleaning(original_string)

def test_string_cleaning_with_case():
	"""Test string_cleaning.
	"""  
	from speechtotext.functions import string_cleaning
	original_string:str = "This needs to be cleaned"
	cleaned_string:str = "this needs to be cleaned"
	assert cleaned_string != string_cleaning(original_string)

def test_string_cleaning_with_special_characters():
	"""Test string_cleaning.
	"""  
	from speechtotext.functions import string_cleaning
	original_string:str = "This needs to be clean?ed///            "
	cleaned_string:str = "This needs to be cleaned"
	assert cleaned_string == string_cleaning(original_string)

