# speechtotext.model.modelWrapper.MetaModelWrapper


### _class_ MetaModelWrapper(name, bases, attrs)
Bases: [`type`](https://docs.python.org/3/library/functions.html#type)

Meta class for model wrapper.

Created to automaticly convert a sample before transcribing.

If the class has a ‘get_transcript_of_file’ method, wrap it

### Methods

| `mro`

 | Return a type's method resolution order.

 |
| `wrap`

                                    | Return a wrapped instance method

                                                               |

#### \__call__(\*args, \*\*kwargs)
Call self as a function.


#### _static_ \__new__(cls, name, bases, attrs)
If the class has a ‘get_transcript_of_file’ method, wrap it


#### mro()
Return a type’s method resolution order.


#### _static_ wrap(get_transcript_of_file)
Return a wrapped instance method
