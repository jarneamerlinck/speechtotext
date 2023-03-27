# PID

## packagename.PID module


### _class_ packagename.PID.PID()
Bases: `object`

Set the Proportional Integral Derivative controller


#### GenOut(error: float)
Calculates error


* **Parameters**

    **error** (*float*) – Value of error



* **Returns**

    PID



* **Return type**

    float



#### Initialize()
Initialize variables


#### SetKd(invar: float)
Set $K_{d}$


* **Parameters**

    **invar** (*float*) – Value to be set in $K_{d}$



#### SetKi(invar: float)
Set $K_{i}$


* **Parameters**

    **invar** (*float*) – Value to be set in $K_{i}$



#### SetKp(invar: float)
Set $K_{p}$


* **Parameters**

    **invar** (*float*) – Value to be set in $K_{p}$



#### SetPrevError(preverror: float)
Sets previous error


* **Parameters**

    **preverror** (*float*) – value of the previous error
