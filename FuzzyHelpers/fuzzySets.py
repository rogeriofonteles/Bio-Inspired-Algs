import numpy as np
import math 

class FuzzySets():

	def __init__(self, intervals):
		self.setIntervals = intervals


	def formFunc(self, points, direction, value):
		midpoint = (points[0]+points[1])/float(2)

		if direction=="crescent":
			return (value - points[0])/float(midpoint - points[0])
		elif direction=="decrescent":
			return (value - points[1])/float(midpoint - points[1])
		elif direction=="constant":
			return 1
		else:
			return "ERROR ON DIRECTION"



class TriangularFuzzySets(FuzzySets):

	def __init__ (self, intervals):
		FuzzySets.__init__(self, intervals)


	def pertinence(self, value):		
		intervalIndex = [x for x in np.array([(i if (value > self.setIntervals[i][0] and value < self.setIntervals[i][1]) else None) for i in range(len(self.setIntervals))]) if x is not None]				
		inferedValues = np.array([self.formFunc(self.setIntervals[i], "crescent", value) if value <= (self.setIntervals[i][0]+self.setIntervals[i][1])/float(2) else self.formFunc(self.setIntervals[i], "decrescent", value) for i in intervalIndex])
		return zip(intervalIndex, inferedValues)



class TrapezoidFuzzySets(FuzzySets):

	def __init__ (self, intervals):
		FuzzySets.__init__(self, intervals)


	def pertinence(self, value):		
		intervalIndex = [x for x in np.array([(i if (value > self.setIntervals[i][0] & value < self.setIntervals[i][3]) else None) for i in range(len(self.setIntervals))]) if x is not None]
		inferedValues = np.array([self.formFunc(self.setIntervals[i], "crescent", value) if value <= self.setIntervals[i][1] else (self.formFunc(self.setIntervals[i], "constant", value) if value <=self.setIntervals[2] else self.formFunc(self.setIntervals[i], "decrescent", value)) for i in intervalIndex])
		return zip(intervalIndex, inferedValues)



class GaussianFuzzySets(FuzzySets):

	def __init__ (self, intervals):
		FuzzySets.__init__(self, intervals)


	def pertinence(self, value):		
		inferedValues = np.array([math.e**(-(1/float(2))*((value-self.setIntervals[i][0])**2)/float(self.setIntervals[i][1])) for i in range(len(self.setIntervals))])
		return zip(range(len(self.setIntervals)), inferedValues)