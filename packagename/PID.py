#! /usr/bin/python
import time
class PID:
	"""Set the Proportional Integral Derivative controller
	"""    
	def __init__(self):
		self.Kp = 0
		self.Kd = 0
		self.Ki = 0
		self.Initialize()

	def SetKp(self,invar:float):
		"""Set $K_{p}$

		Args:
			invar (float): Value to be set in $K_{p}$
		"""     
		self.Kp = invar

	def SetKi(self,invar:float):
		"""Set $K_{i}$

		Args:
			invar (float): Value to be set in $K_{i}$
		"""     
		self.Ki = invar

	def SetKd(self,invar:float):
		"""Set $K_{d}$

		Args:
			invar (float): Value to be set in $K_{d}$
		"""      
		self.Kd = invar

	def SetPrevError(self,preverror:float):
		"""Sets previous error

		Args:
			preverror (float): value of the previous error
		"""     
		self.prev_error = preverror

	def Initialize(self):
		"""Initialize variables
		"""     
		self.currtime = time.time()
		self.prevtime = self.currtime

		self.prev_error = 0

		self.Cp = 0
		self.Ci = 0
		self.Cd = 0

	def GenOut(self,error:float) -> float:
		"""Calculates error

		Args:
			error (float): Value of error

		Returns:
			float: PID
		"""     
		self.currtime = time.time()
		dt = self.currtime - self.prevtime
		de = error - self.prev_error

		self.Cp = self.Kp*error
		self.Ci += error*dt

		self.Cd = 0
		if dt > 0:
			self.Cd = de/dt

		self.prevtime = self.currtime
		self.prev_error = error

		return self.Cp + (self.Ki*self.Ci) + (self.Kd*self.Cd)


