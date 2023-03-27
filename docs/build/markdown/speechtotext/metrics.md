# Metrics

## speechtotext.metrics module


### _class_ speechtotext.metrics.Metrics(reference: str, hypothesis: str, with_cleaning=True)
Bases: `object`

_summary_
.. attribute:: class_attribute

> (class attribute) The class attribute


> * **type**

>     str



#### wer()
(class attribute) word error rate (WER)


* **Type**

    float



#### mer()
(class attribute) match error rate (MER)


* **Type**

    float



#### wil()
(class attribute) word information lost (WIL)


* **Type**

    float



#### wip()
(class attribute) word information preserved (WIP)


* **Type**

    float



#### cer()
(class attribute) character error rate (CER)


* **Type**

    float



### speechtotext.metrics.notebook_metrics_print(dataset, id: str, hypothesis: str)
