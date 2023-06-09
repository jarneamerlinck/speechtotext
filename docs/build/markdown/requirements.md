# Requirements for speechtotext

## Overview

Requirements for the speechtotext package:


* Folder with datasets and the `transcripts.txt` to test the models.


* Contents of `.env` in the directory of the python script.

## Content of .env

### Whisper API

```shell
OPENAI_API_KEY=sk-somemorerandomnumberlettersandmorerandomnessform
OPENAI_ORGANIZATION=org-somerandomnumberandlette
```

### Amazon transcribe

```shell
AWS_ACCESS_KEY_ID=access-id
AWS_SECRET_ACCESS_KEY=acces-key
AMAZON_REGION=eu-west-3
AMAZON_BUCKET=bucket-name
```


* For bucket with name `foo` following command returns the region.

```shell
curl -sI foo.s3.amazonaws.com | awk '/^x-amz-bucket-region:/ { print $2 }'
```

### Google API

This is the file for an service account.  [Link to google cloud docs](https://developers.google.com/workspace/guides/create-credentials).

```shell
GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
```

### Deepgram API

```shell
DEEPGRAM_API_KEY=somemorerandomnumberlettersandmorerandomnessform
```

### AssemblyAI API

```shell
ASSEMBLY_AI_API_KEY=somemorerandomnumberlettersandmorerandomnessform
```

### Azure API

```shell
AZURE_SPEECH_KEY=somemorerandomnumberlettersandmorerandomnessform
AZURE_SPEECH_REGION=somemorerandomnumberlettersandmorerandomnessform
```

### Speechmatics API

```shell
SPEECHMATICS_API_KEY=somemorerandomnumberlettersandmorerandomnessform
```
