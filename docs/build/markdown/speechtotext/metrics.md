# Metrics

## speechtotext.metrics module

Module that calculates the metrics for speechtotext models.

Use this module like this:

```python
# Imports
from speechtotext.metrics import Metrics

# Create metrics
m = Metrics("De stoel heeft krassen gemaakt op de vloer!", "De stoel heeft krassen gemaakt op de vloer", "id_from_dataset")
print(m)
```


### _class_ speechtotext.metrics.Metrics(reference: str, hypothesis: str, audio_id: str, with_cleaning=True)
Bases: `object`

Class to calulate the metrics.
.. attribute:: class_attribute

> (class attribute) The class attribute.


> * **type**

>     str



#### wer()
(class attribute) word error rate (WER).


* **Type**

    float



#### mer()
(class attribute) match error rate (MER).


* **Type**

    float



#### wil()
(class attribute) word information lost (WIL).


* **Type**

    float



#### wip()
(class attribute) word information preserved (WIP).


* **Type**

    float



#### cer()
(class attribute) character error rate (CER).


* **Type**

    float



### speechtotext.metrics.notebook_metrics_print(dataset: [Dataset](datasets.md#speechtotext.datasets.Dataset), id: str, hypothesis: str)
Print metrics from transcript and hypothesis.


* **Parameters**

    
    * **dataset** ([*Dataset*](datasets.md#speechtotext.datasets.Dataset)) – dataset of audio.


    * **id** (*str*) – id of the audio file.


    * **hypothesis** (*str*) – hypothesis transcript.
