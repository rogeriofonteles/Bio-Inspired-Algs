import numpy as np
import random
import math
from fileHelper import FileExtractor

class NeuralNetwork():

	def __init__(self, _inputMatrix, _outputMatrix):		
		self.inputMatrix = np.c_[ [-1 for i in range(len(_inputMatrix))], _inputMatrix ]				
		self.outputMatrix = _outputMatrix		
		#self.outputMatrix[self.outputMatrix < 1] = -1		
		self.trainingIndexes(_inputMatrix)		
		self.confusionMatrix = np.zeros((len(_outputMatrix[0]), len(_outputMatrix[0])+1))		


	def trainingIndexes(self, matrix):		
		self.testIndex = random.sample(range(len(matrix)), int(math.floor(len(matrix)/float(5.0))))
		#self.testIndex = []


	def accuracy(self):		
		accuracy = 100*(sum([self.confusionMatrix[i][i] for i in range(len(self.outputMatrix[0]))])/float(self.confusionMatrix.sum()))
		return accuracy


	def classAccuracy(self):
		classAccuracy = [100*(self.confusionMatrix[i][i])/float(self.confusionMatrix[i].sum()) for i in range(len(self.outputMatrix[0]))]
		return classAccuracy


	def separateTraining(self, matrix):		
		training = []
		test = []
		[(test.append(matrix[i])) if i in self.testIndex else training.append(matrix[i]) for i in range(len(matrix))]
		return training, test



class Perceptron():

	def __init__(self, learningFactor, inputSize, _activationFunction):
		self.eta = learningFactor
		self.w = 0.01*np.random.rand(inputSize)
		self.activationFunction = _activationFunction


	def training(self, neuronInput, localGradient):
		self.w = self.w + self.eta*localGradient*np.array(neuronInput)


	def testing(self, testingExample):
		return self.activationFunction.run(self.w.dot(testingExample))