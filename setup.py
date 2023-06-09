#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'speechtotext'
INSTALL_NAME = 'speechtotext-python'
DESCRIPTION = 'Python package to benchmark speech2text models.'
URL = 'https://github.com/jarneamerlinck/speechtotext'
EMAIL = 'jarneamerlinck@gmail.com'
AUTHOR = 'Jarne Amerlinck'
REQUIRES_PYTHON = '>=3.9.2,<3.11'
VERSION = '' # Version is defined in __version__.py in the package

# What packages are required for this module to be executed?
REQUIRED = [
	'jiwer==3.0.1', 'pandas<2.0.0', 'numpy', 'torch>=2.0.0', 
	'openai-whisper', 'openai', 'python-dotenv',
	'matplotlib', 'ipywidgets', 'nbformat','seaborn',
	'dtale', 'boto3', 'google-cloud-speech',
	'deepgram-sdk', 'azure-cognitiveservices-speech', 
	'speechmatics-python==1.6.4', 'pydub', 'docstring_parser',
	'nltk', 'rouge'
]

# What packages are optional?
EXTRAS = {
	'docs': ['Sphinx>=6.1.3', 'sphinx-markdown-builder>=0.5.5', 'sphinx_autodoc_typehints>=1.22', 
			 'sphinx-rtd-theme', 'sphinx_favicon', 'twine', 'graphviz', 'nbsphinx']
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
	with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
		long_description = '\n' + f.read()
except FileNotFoundError:
	long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
	project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
	with open(os.path.join(here, project_slug, '__version__.py')) as f:
		exec(f.read(), about)
else:
	about['__version__'] = VERSION


class UploadCommand(Command):
	"""Support setup.py upload."""

	description = 'Build and publish the package.'
	user_options = []

	@staticmethod
	def status(s):
		"""Prints things in bold."""
		print('\033[1m{0}\033[0m'.format(s))

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		try:
			self.status('Removing previous builds…')
			rmtree(os.path.join(here, 'dist'))
		except OSError:
			pass

		self.status('Building Source and Wheel (universal) distribution…')
		os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

		self.status('Uploading the package to PyPI via Twine…')
		os.system('twine upload dist/*')

		self.status('Pushing git tags…')
		os.system('git tag v{0}'.format(about['__version__']))
		os.system('git push --tags')

		sys.exit()


# Where the magic happens:


setup(
	name=INSTALL_NAME,
	version=about['__version__'],
	description=DESCRIPTION,
	long_description=long_description,
	long_description_content_type='text/markdown',
	author=AUTHOR,
	author_email=EMAIL,
	python_requires=REQUIRES_PYTHON,
	url=URL,
	packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
	# If your package is a single module, use this instead of 'packages':
	# py_modules=['mypackage'],

	# entry_points={
	#     'console_scripts': ['mycli=mymodule:cli'],
	# },
	install_requires=REQUIRED,
	extras_require=EXTRAS,
	include_package_data=True,
	license='MIT',
	classifiers=[
		# Trove classifiers
		# Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: Implementation :: PyPy'
	],
	# $ setup.py publish support.
	cmdclass={
		'upload': UploadCommand,
	},
)
