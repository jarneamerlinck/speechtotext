import unittest

class TestImport(unittest.TestCase):
	def test_module_import(self):
		"""Test base import.
		"""    
		import speechtotext.functions
class TestCuda(unittest.TestCase):
 
	def test_force_cudnn_initialization(self):
		"""Test force_cudnn_initialization.
		""" 
		from speechtotext.functions import force_cudnn_initialization
		force_cudnn_initialization()
class TestCleanString(unittest.TestCase):

	def test_string_cleaning_same(self):
		"""Test string_cleaning.
		"""  
		from speechtotext.functions import string_cleaning
		original_string:str = "This needs to be cleaned"
		cleaned_string:str = "This needs to be cleaned"
		self.assertEquals(cleaned_string,string_cleaning(original_string))
	def test_string_cleaning_diff(self):
		"""Test string_cleaning.
		"""  
		from speechtotext.functions import string_cleaning
		original_string:str = "This needs to be cleanedd"
		cleaned_string:str = "This needs to be cleaned"
		self.assertNotEqual(cleaned_string, string_cleaning(original_string))

	def test_string_cleaning_diff_number(self):
		"""Test string_cleaning.
		"""  
		from speechtotext.functions import string_cleaning
		original_string:str = "This needs to 3be cleaned"
		cleaned_string:str = "This needs to be cleaned"
		self.assertNotEqual( cleaned_string,string_cleaning(original_string))

	def test_string_cleaning_with_case(self):
		"""Test string_cleaning.
		"""  
		from speechtotext.functions import string_cleaning
		original_string:str = "This needs to be cleaned"
		cleaned_string:str = "this needs to be cleaned"
		self.assertNotEqual( cleaned_string, string_cleaning(original_string))
	def test_string_cleaning_with_special_characters(self):
		"""Test string_cleaning.
		"""  
		from speechtotext.functions import string_cleaning
		original_string:str = "This needs to be clean?ed///            "
		cleaned_string:str = "This needs to be cleaned"
		self.assertEqual( cleaned_string,string_cleaning(original_string))

class TestFilesAndFolders(unittest.TestCase):

	def test_join_benchmark_results_without_index(self):
		"""Test join_benchmark_results.
		"""  
		from speechtotext.functions import join_benchmark_results
		import pandas as pd
		import pandas as pd
		column_names = ["model_name","audio_ID","dataset","reference","message"]
		string1 = """Whisper_medium,20000_mijlen_6038,20000_mijlen,"Tegen vijf uur",CUDA out of memory
Whisper_medium,20000_mijlen_4306,20000_mijlen,"de stuurman maakte daarvan gebruik",CUDA out of memory"""

		string2 = """Whisper_medium,vl06228,RDH_VL,Gerechtelijke stappen,CUDA out of memory
Whisper_medium,vl07041,RDH_VL,Het is niet mijn bedoeling,CUDA out of memory"""
		df1 = pd.DataFrame([x.split(',') for x in string1.split('\n')], columns=column_names)
		df2 = pd.DataFrame([x.split(',') for x in string2.split('\n')], columns=column_names)
		string_full="""Whisper_medium,20000_mijlen_6038,20000_mijlen,"Tegen vijf uur",CUDA out of memory
Whisper_medium,20000_mijlen_4306,20000_mijlen,"de stuurman maakte daarvan gebruik",CUDA out of memory
Whisper_medium,vl06228,RDH_VL,Gerechtelijke stappen,CUDA out of memory
Whisper_medium,vl07041,RDH_VL,Het is niet mijn bedoeling,CUDA out of memory"""
		df_full = pd.DataFrame([x.split(',') for x in string_full.split('\n')], columns=column_names)
		df_gen = join_benchmark_results([df1, df2], set_index=False)
	
		self.assertTrue((df_gen == df_full).all().all())

	def test_join_benchmark_results_with_index(self):
		"""Test join_benchmark_results.
		"""  
		from speechtotext.functions import join_benchmark_results
		import pandas as pd
		column_names = ["model_name","audio_ID","dataset","reference","message"]
		string1 = """Whisper_medium,20000_mijlen_6038,20000_mijlen,"Tegen vijf uur",CUDA out of memory
Whisper_medium,20000_mijlen_4306,20000_mijlen,"de stuurman maakte daarvan gebruik",CUDA out of memory"""

		string2 = """Whisper_medium,vl06228,RDH_VL,Gerechtelijke stappen,CUDA out of memory
Whisper_medium,vl07041,RDH_VL,Het is niet mijn bedoeling,CUDA out of memory"""
		df1 = pd.DataFrame([x.split(',') for x in string1.split('\n')], columns=column_names)
		df2 = pd.DataFrame([x.split(',') for x in string2.split('\n')], columns=column_names)
		string_full="""Whisper_medium,20000_mijlen_6038,20000_mijlen,"Tegen vijf uur",CUDA out of memory
Whisper_medium,20000_mijlen_4306,20000_mijlen,"de stuurman maakte daarvan gebruik",CUDA out of memory
Whisper_medium,vl06228,RDH_VL,Gerechtelijke stappen,CUDA out of memory
Whisper_medium,vl07041,RDH_VL,Het is niet mijn bedoeling,CUDA out of memory"""
		df_full = pd.DataFrame([x.split(',') for x in string_full.split('\n')], columns=column_names).set_index(["model_name", "audio_ID"])
		df_gen = join_benchmark_results([df1, df2], set_index=True)
	
		self.assertTrue((df_gen == df_full).all().all())

	def test_separate_benchmark_results_by_model(self):
		"""Test join_benchmark_results.
		"""  
		from speechtotext.functions import separate_benchmark_results_by_model
		import pandas as pd
		column_names = ["model_name","audio_ID","dataset","duration","reference","wer","mer","wil","wip","cer"]
		string1 = """Whisper_tiny,20000_mijlen_3159.wav,20000_mijlen,0.9828286170959473,Toen de zonshoogte genomen was ging ik naar den salon en zag dat wij naar hetgeen op de kaart werd aangeteekend,0.5714285714285714,0.5714285714285714,0.7969924812030076,0.20300751879699247,0.1981981981981982
Whisper_tiny,20000_mijlen_2691.wav,20000_mijlen,0.8778934478759766,Neen kapitein maar er bestaat nog een ander gevaar Welk mijnheer,1.0,0.7333333333333333,0.9030303030303031,0.09696969696969697,0.328125"""

		string2 = """Whisper_small,20000_mijlen_3159.wav,20000_mijlen,3.7967710494995117,Toen de zonshoogte genomen was ging ik naar den salon en zag dat wij naar hetgeen op de kaart werd aangeteekend,0.38095238095238093,0.36363636363636365,0.5555555555555556,0.4444444444444444,0.11711711711711711
Whisper_small,20000_mijlen_2691.wav,20000_mijlen,3.3797714710235596,Neen kapitein maar er bestaat nog een ander gevaar Welk mijnheer,0.45454545454545453,0.45454545454545453,0.7024793388429753,0.29752066115702475,0.15625"""
		df1 = pd.DataFrame([x.split(',') for x in string1.split('\n')], columns=column_names)
		df2 = pd.DataFrame([x.split(',') for x in string2.split('\n')], columns=column_names)
		string_full="""Whisper_tiny,20000_mijlen_3159.wav,20000_mijlen,0.9828286170959473,Toen de zonshoogte genomen was ging ik naar den salon en zag dat wij naar hetgeen op de kaart werd aangeteekend,0.5714285714285714,0.5714285714285714,0.7969924812030076,0.20300751879699247,0.1981981981981982
Whisper_tiny,20000_mijlen_2691.wav,20000_mijlen,0.8778934478759766,Neen kapitein maar er bestaat nog een ander gevaar Welk mijnheer,1.0,0.7333333333333333,0.9030303030303031,0.09696969696969697,0.328125
Whisper_small,20000_mijlen_3159.wav,20000_mijlen,3.7967710494995117,Toen de zonshoogte genomen was ging ik naar den salon en zag dat wij naar hetgeen op de kaart werd aangeteekend,0.38095238095238093,0.36363636363636365,0.5555555555555556,0.4444444444444444,0.11711711711711711
Whisper_small,20000_mijlen_2691.wav,20000_mijlen,3.3797714710235596,Neen kapitein maar er bestaat nog een ander gevaar Welk mijnheer,0.45454545454545453,0.45454545454545453,0.7024793388429753,0.29752066115702475,0.15625"""
		df_full = pd.DataFrame([x.split(',') for x in string_full.split('\n')], columns=column_names)

		list_gen = separate_benchmark_results_by_model(df_full)
		del df1["model_name"]
		del df2["model_name"]

		self.assertTrue((list_gen["Whisper_tiny"].reset_index()== df1).all().all())
		self.assertTrue((list_gen["Whisper_small"].reset_index() == df2).all().all())


	def test_benchmark_results_to_csv(self):
		"""Test join_benchmark_results.
		"""
		from speechtotext.functions import benchmark_results_to_csv
		import pandas as pd
		import os
		save_name = ".test_file_save.csv"
		column_names = ["model_name","audio_ID","dataset","reference","message"]
		string1 = """Whisper_medium,20000_mijlen_6038,20000_mijlen,"Tegen vijf uur",CUDA out of memory
Whisper_medium,20000_mijlen_4306,20000_mijlen,"de stuurman maakte daarvan gebruik",CUDA out of memory"""

		string2 = """Whisper_medium,vl06228,RDH_VL,Gerechtelijke stappen,CUDA out of memory
Whisper_medium,vl07041,RDH_VL,Het is niet mijn bedoeling,CUDA out of memory"""
		df1 = pd.DataFrame([x.split(',') for x in string1.split('\n')], columns=column_names)
		df2 = pd.DataFrame([x.split(',') for x in string2.split('\n')], columns=column_names)
		string_full="""Whisper_medium,20000_mijlen_6038,20000_mijlen,"Tegen vijf uur",CUDA out of memory
Whisper_medium,20000_mijlen_4306,20000_mijlen,"de stuurman maakte daarvan gebruik",CUDA out of memory
Whisper_medium,vl06228,RDH_VL,Gerechtelijke stappen,CUDA out of memory
Whisper_medium,vl07041,RDH_VL,Het is niet mijn bedoeling,CUDA out of memory"""
		df_full = pd.DataFrame([x.split(',') for x in string_full.split('\n')], columns=column_names)
		benchmark_results_to_csv(results=[df1, df2], save_name=save_name)
		
		self.assertTrue(os.path.exists(save_name))
		self.assertTrue( (pd.read_csv(save_name) == df_full).all().all())
	
		os.remove(save_name)
		self.assertFalse(os.path.exists(save_name))

	def test_save_sub_folder_name(self):
		"""Test save_sub_folder_name.
		"""
		from speechtotext.functions import save_sub_folder_name
		import pandas as pd
		import os
		sub_folder = "test_to_remove"
		
		self.assertFalse(os.path.isdir(sub_folder))
		save_sub_folder_name(".", sub_folder)
		self.assertTrue( os.path.isdir(sub_folder))
		os.rmdir(sub_folder)
		self.assertFalse(os.path.isdir(sub_folder))
		
	def test_save_folder_name(self):
		"""Test save_folder_name.
		"""
		import speechtotext
		from speechtotext.functions import save_folder_name
		from datetime import datetime
		import os
		folder_name = "."
		report_name = "report_name"
		datetime_folder = datetime.now().strftime('%Y_%m_%d_%H_%M_%S') 
		speechtotext.functions.DEFAULT_DATETIME_FORMAT = datetime_folder
		check_folder_name =  f"{folder_name}/{report_name}_{datetime_folder}"
		
		self.assertFalse( os.path.isdir(check_folder_name))
		save_folder_name(report_name, folder_name)
		self.assertTrue( os.path.isdir(check_folder_name))
		os.rmdir(check_folder_name)
		self.assertFalse( os.path.isdir(check_folder_name)	)

	def test_get_extention_of_file_name(self):
		"""Test get_extention_of_file_name.
		"""
		from speechtotext.functions import get_extention_of_file_name
		import os
		file_name = "config.txt"
		_ , file_extension = os.path.splitext(file_name) 
		self.assertEqual( file_extension,get_extention_of_file_name(file_name))

	def test_get_file_name_without_extentione(self):
		"""Test get_file_name_without_extention.
		"""
		from speechtotext.functions import get_file_name_without_extention
		import os
		file_name = "config.txt"
		name , _ = os.path.splitext(file_name) 
		self.assertEqual(  name ,get_file_name_without_extention(file_name))
class TestStrings(unittest.TestCase): 
	def test_uppercase_for_first_character_in_string_no_change(self):
		"""Test uppercase_for_first_character_in_string.
		"""
		from speechtotext.functions import uppercase_for_first_character_in_string
		original = "Thsi is not more then we need"
		check = "Thsi is not more then we need"
		self.assertEqual( check , uppercase_for_first_character_in_string(original))

	def test_uppercase_for_first_character_in_string_change(self):
		"""Test uppercase_for_first_character_in_string.
		"""
		from speechtotext.functions import uppercase_for_first_character_in_string
		original = "thsi is not more then we need"
		check = "Thsi is not more then we need"
		self.assertEqual( check , uppercase_for_first_character_in_string(original))
	
	def test_uppercase_for_first_character_in_string_all_upper(self):
		"""Test uppercase_for_first_character_in_string.
		"""
		from speechtotext.functions import uppercase_for_first_character_in_string
		original = "THSI IS NOT MORE THEN WE NEED"
		check = "THSI IS NOT MORE THEN WE NEED"
		self.assertEqual( check ,uppercase_for_first_character_in_string(original))
 
	def test_multidispatch(self):
		"""Test multidispatch.
		"""
		from speechtotext.functions import multidispatch
		class TestClass():
			number = 3

			@multidispatch(int)
			def update_number(self, new_number: int):
				self.number =  new_number
			@multidispatch(int, int)
			def update_number(self, new_number: int, new_number2:int):
				self.number =  new_number+new_number2
		
		t = TestClass()
		
		t.update_number(4)
		self.assertEqual( t.number , 4)
		
		t.update_number(4, -2)
		self.assertEqual(t.number, 2)

class TestEnv(unittest.TestCase):
	def test_load_env_variable(self):
		"""Test load_env_variable.
		"""
		from speechtotext.functions import load_env_variable 
		import os
		os_env = "5"
		os.environ["os_env"] = "5"
		self.assertEqual(os_env, load_env_variable("os_env"))

	def test_load_env_variable_exception(self):
		"""Test load_env_variable.
		"""
		from speechtotext.functions import load_env_variable, RequiredEnvVariablesMissing
		import os
		os.environ.pop("os_env")
		def func():
			load_env_variable("os_env")
		self.assertRaises(RequiredEnvVariablesMissing, func)
  
class TestTiming(unittest.TestCase):
	def test_load_env_variable_exception(self):
		"""Test load_env_variable.
		"""
		from speechtotext.functions import timing
		import os
		@timing
		def func_slow():
			[i for i in range(2000)]
		@timing
		def func_fast():
			[i for i in range(200)]
		self.assertTrue(func_slow() > func_fast())
  
