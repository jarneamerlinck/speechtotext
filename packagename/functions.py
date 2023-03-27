#!/usr/bin/env python
import threading
import os

def set_max_limit(value:int, max:int) -> int:
	"""Set maximum limit for an value

	Args:
		value (int): value
		max (int): maximum

	Returns:
		int: maximum of the 2 values
	""" 
	return max if value > max else value

def set_min_limit(value:int, min:int) -> int:
	"""Set minimum limit for an value

	Args:
		value (int): value
		min (int): minimum

	Returns:
		int: minimum of the 2 values
	"""    
	return min if value < min else value


class ThreadSafeSingleton(type):
	"""Class to create ThreadSafeSingleton

	Returns:
		ThreadSafeSingleton: Class object
	"""    
	_instances = {}
	_singleton_locks: dict[any, threading.Lock] = {}

	def __call__(cls, *args, **kwargs):
		# double-checked locking pattern (https://en.wikipedia.org/wiki/Double-checked_locking)
		if cls not in cls._instances:
			if cls not in cls._singleton_locks:
				cls._singleton_locks[cls] = threading.Lock()
			with cls._singleton_locks[cls]:
				if cls not in cls._instances:
					cls._instances[cls] = super(ThreadSafeSingleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]


def device_exists(path:str) -> bool:
	"""This functions checks if an device exists in linux

	Args:
		path (str): Path to device  (/dev/tty for example)

	Returns:
		bool: True if device exists
	"""    
	try:
		os.stat(path)
	except OSError:
		return False
	return True




