Requirements for speechtotext
=============================

Overview
++++++++

Requirements for the speechtotext package:

* Folder with datasets and the ``transcripts.txt`` to test the models.

* Contents of ``.env`` in the directory of the python script.



Content of .env
+++++++++++++++

Whisper API
-----------

.. code-block:: shell

	OPENAI_API_KEY=sk-somemorerandomnumberlettersandmorerandomnessform
	OPENAI_ORGANIZATION=org-somerandomnumberandlette

Amazon transcribe
-----------------
.. code-block:: shell

	AWS_ACCESS_KEY_ID=access-id
	AWS_SECRET_ACCESS_KEY=acces-key
	AMAZON_REGION=eu-west-3
	AMAZON_BUCKET=bucket-name

* For bucket with name ``foo`` following command returns the region.

.. code-block:: shell

	curl -sI foo.s3.amazonaws.com | awk '/^x-amz-bucket-region:/ { print $2 }'

Google API
----------

This is the file for an service account.  `Link to google cloud docs <https://developers.google.com/workspace/guides/create-credentials>`_.



.. code-block:: shell

	GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"