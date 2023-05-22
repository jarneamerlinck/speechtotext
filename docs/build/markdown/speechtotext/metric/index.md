# speechtotext metric package

## metrics

Module that calculates the metrics for speechtotext models.

Use this module like this:

```python
# Imports
from speechtotext.metric.metrics import Metrics

# Create metrics
m = Metrics("This is the original text, the source.", "This is the hypothesis text..", "id_from_dataset", duration=0.5)
print(m)
```


### _class_ speechtotext.metric.metrics.Metrics(reference: str, hypothesis: str, audio_id: str, duration: float, with_cleaning=True)
Bases: `object`

Class to calulate the metrics.


#### wer()
Word error rate (WER).

The WER is how many words there were made errors on.


* **Type**

    float



#### mer()
Match error rate (MER).

The MER indicates the percentage of words that were incorrectly predicted and inserted.


* **Type**

    float



#### wil()
Word information lost (WIL).

The WIL represents the word information that is lost.


* **Type**

    float



#### wip()
Word information preserved (WIP).

The WIP represents the word information that is preserved.


* **Type**

    float



#### cer()
Character error rate (CER).

The CER is how many characters there were made errors on.


* **Type**

    float



#### substitutions()
Number of words substituted (substitutions).

The substitutions is the number of words that were replaced.


* **Type**

    int



#### insertions()
Number of words inserted (insertions).

The insertions is the number of words that were added.


* **Type**

    int



#### hits()
Number of words correct (hits).

The hits is the number of words correctly predicted.


* **Type**

    int



#### deletions()
Number of words deleted (deletions).

The deletions is the number of words that were removed.


* **Type**

    int



#### duration()
Duration of the transcribing (duration).

The duration is how long it took to transcribe the audiofile.


* **Type**

    float



#### meteor()
Metric for Evaluation of Translation with Explicit ORdering (METEOR).

METEOR is an automatic metric for machine translation evaluation that is based on a generalized concept of
unigram matching between the machine-produced translation and human-produced reference translations.


* **Type**

    float



#### bleu()
Bilingual Evaluation Understudy (BLEU).

BLEU is used in comparing a candidate translation to one or more reference translations.


* **Type**

    float



#### rouge_1_r()
Recall-Oriented Understudy for Gisting Evaluation recall of 1-grams (ROUGE-1-r).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-1-r is the recall of 1-grams.


* **Type**

    float



#### rouge_1_p()
Recall-Oriented Understudy for Gisting Evaluation precision of 1-grams (ROUGE-1-p).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-1-p is the precision of 1-grams.


* **Type**

    float



#### rouge_1_f()
Recall-Oriented Understudy for Gisting Evaluation F1-score of 1-grams (ROUGE-1-f).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-1-f is the F1-score of 1-grams.


* **Type**

    float



#### rouge_2_r()
Recall-Oriented Understudy for Gisting Evaluation recall of 2-grams (ROUGE-2-r).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-2-r is the recall of 2-grams.


* **Type**

    float



#### rouge_2_p()
Recall-Oriented Understudy for Gisting Evaluation precision of 2-grams (ROUGE-2-p).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-2-p is the precision of 2-grams.


* **Type**

    float



#### rouge_2_f()
Recall-Oriented Understudy for Gisting Evaluation F1-score of 2-grams (ROUGE-2-f).

ROUGE includes measures to automatically determine the quality of a summary
by comparing it to other (ideal) summaries created by humans.
ROUGE-2-f is the F1-score of 2-grams.


* **Type**

    float



#### rouge_l_r()
Recall-Oriented Understudy for Gisting Evaluation recall of LCS (ROUGE-L-r).

ROUGE-L is based on the longest common subsequence (LCS) between our model output and reference.
ROUGE-L-r is the recall of LCS.


* **Type**

    float



#### rouge_l_p()
Recall-Oriented Understudy for Gisting Evaluation precision of LCS (ROUGE-L-p).

ROUGE-L is based on the longest common subsequence (LCS) between our model output and reference.
ROUGE-l-p is the precision of LCS.


* **Type**

    float



#### rouge_l_f()
Recall-Oriented Understudy for Gisting Evaluation F1-score of LCS (ROUGE-L-f).

ROUGE-L is based on the longest common subsequence (LCS) between our model output and reference.
ROUGE-L-f is the F1-score of LCS.


* **Type**

    float



#### \__call__(\*args, \*\*kwds)
Calculate the metrics.


#### get_all_metric_docs()
Returns all descriptions of metrics returned by get_all_metric_names in the correct order.


* **Returns**

    List of all metric descriptions.



* **Return type**

    list[str]



#### get_all_metric_names()
Returns all possible metric names in a list.


* **Returns**

    List of all metric names.



* **Return type**

    list[str]


## customMetrics

Module to create custom metrics to save with the plots from the plotting module.

Use this module like this:

```python
# Imports
from speechtotext.functions import BaseResult
from speechtotext.plot.plotting import Plotting

# Create class with matplotlib picture
class BenchmarkResults(BaseMetrics):
        def create_df(self) -> pd.core.frame.DataFrame:
                return self.df

# Add model to Plotting
Plotting.CUSTOM_RESULTS.append(BenchmarkResults)
```


### _class_ speechtotext.metric.customMetrics.BaseMetrics(df: DataFrame, report_folder: str, file_name: str)
Bases: [`BaseResult`](../index.md#speechtotext.functions.BaseResult)

Base class used to create metrics for result dataframe.


#### _abstract_ create_df()
Creates df that needs to be saved.


* **Returns**

    Dataframe that needs to be saved.



* **Return type**

    pd.core.frame.DataFrame



#### save()
Saves Result to report folder.


### _class_ speechtotext.metric.customMetrics.BenchmarkResults(df: DataFrame, report_folder: str, file_name: str)
Bases: `BaseMetrics`

This class saves the results of the benchmark.


#### create_df()
Creates df that needs to be saved.


* **Returns**

    Dataframe that needs to be saved.



* **Return type**

    pd.core.frame.DataFrame



### _class_ speechtotext.metric.customMetrics.ErrorMetrics(df: DataFrame, report_folder: str, file_name: str)
Bases: `BaseMetrics`

This class calulates the error statistic on the benchmark results.


#### create_df()
Creates df that needs to be saved.


* **Returns**

    Dataframe that needs to be saved.



* **Return type**

    pd.core.frame.DataFrame



### _class_ speechtotext.metric.customMetrics.ResultMetrics(df: DataFrame, report_folder: str, file_name: str)
Bases: `BaseMetrics`

This class calulates the default statistic metrics on the benchmark results.


#### create_df()
Creates df that needs to be saved.


* **Returns**

    Dataframe that needs to be saved.



* **Return type**

    pd.core.frame.DataFrame
