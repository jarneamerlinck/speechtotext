# speechtotext.metric.metrics.Metrics


### _class_ Metrics(reference, hypothesis, audio_id, duration, with_cleaning=True)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Class to calulate the metrics.


#### wer()
Word error rate (WER).

The WER is how many words there were made errors on.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### mer()
Match error rate (MER).

The MER indicates the percentage of words that were incorrectly predicted and inserted.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### wil()
Word information lost (WIL).

The WIL represents the word information that is lost.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### wip()
Word information preserved (WIP).

The WIP represents the word information that is preserved.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### cer()
Character error rate (CER).

The CER is how many characters there were made errors on.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### substitutions()
Number of words substituted (substitutions).

The substitutions is the number of words that were replaced.


* **Type**

    [int](https://docs.python.org/3/library/functions.html#int)



#### insertions()
Number of words inserted (insertions).

The insertions is the number of words that were added.


* **Type**

    [int](https://docs.python.org/3/library/functions.html#int)



#### hits()
Number of words correct (hits).

The hits is the number of words correctly predicted.


* **Type**

    [int](https://docs.python.org/3/library/functions.html#int)



#### deletions()
Number of words deleted (deletions).

The deletions is the number of words that were removed.


* **Type**

    [int](https://docs.python.org/3/library/functions.html#int)



#### duration()
Duration of the transcribing (duration).

The duration is how long it took to transcribe the audiofile.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### meteor()
Metric for Evaluation of Translation with Explicit ORdering (METEOR).

METEOR is an automatic metric for machine translation evaluation that is based on a generalized concept of
unigram matching between the machine-produced translation and human-produced reference translations.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### bleu()
Bilingual Evaluation Understudy (BLEU).

BLEU is used in comparing a candidate translation to one or more reference translations.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### rouge_1_r()
Recall-Oriented Understudy for Gisting Evaluation recall of 1-grams (ROUGE-1-r).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-1-r is the recall of 1-grams.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### rouge_1_p()
Recall-Oriented Understudy for Gisting Evaluation precision of 1-grams (ROUGE-1-p).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-1-p is the precision of 1-grams.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### rouge_1_f()
Recall-Oriented Understudy for Gisting Evaluation F1-score of 1-grams (ROUGE-1-f).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-1-f is the F1-score of 1-grams.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### rouge_2_r()
Recall-Oriented Understudy for Gisting Evaluation recall of 2-grams (ROUGE-2-r).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-2-r is the recall of 2-grams.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### rouge_2_p()
Recall-Oriented Understudy for Gisting Evaluation precision of 2-grams (ROUGE-2-p).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-2-p is the precision of 2-grams.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### rouge_2_f()
Recall-Oriented Understudy for Gisting Evaluation F1-score of 2-grams (ROUGE-2-f).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-2-f is the F1-score of 2-grams.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### rouge_l_r()
Recall-Oriented Understudy for Gisting Evaluation recall of LCS (ROUGE-L-r).

ROUGE-L is based on the longest common subsequence (LCS) between our model output and reference.
ROUGE-L-r is the recall of LCS.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### rouge_l_p()
Recall-Oriented Understudy for Gisting Evaluation precision of LCS (ROUGE-L-p).

ROUGE-L is based on the longest common subsequence (LCS) between our model output and reference.
ROUGE-l-p is the precision of LCS.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)



#### rouge_l_f()
Recall-Oriented Understudy for Gisting Evaluation F1-score of LCS (ROUGE-L-f).

ROUGE-L is based on the longest common subsequence (LCS) between our model output and reference.
ROUGE-L-f is the F1-score of LCS.


* **Type**

    [float](https://docs.python.org/3/library/functions.html#float)


Class to calulate the metrics.


* **Parameters**

    
    * **reference** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Reference transcript.


    * **hypothesis** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Hypothesis transcript.


    * **audio_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Id of the audio file.


    * **with_cleaning** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Set True to clean transcripts. Defaults to True.


### Methods

| `get_all_metric_docs`

 | Returns all descriptions of metrics returned by get_all_metric_names in the correct order.

 |
| `get_all_metric_names`

                    | Returns all possible metric names in a list.

                                               |

#### \__call__(\*args, \*\*kwds)
Calculate the metrics.


#### get_all_metric_docs()
Returns all descriptions of metrics returned by get_all_metric_names in the correct order.


* **Returns**

    List of all metric descriptions.



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]



#### get_all_metric_names()
Returns all possible metric names in a list.


* **Returns**

    List of all metric names.



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]
