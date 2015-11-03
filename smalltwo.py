import math
import operator


def euclideanDistance(firstPoint, secondPoint, length):
	#Calculate the distance between firstPoint and secondPoint, which are arrays of size length.
	distance = 0
	for i in xrange(length):
		paramDifference = firstPoint[i] - secondPoint[i]
		distance += pow(paramDifference, 2)
	return math.sqrt(distance)
  
  

class Sample(object):
  #Represents a single data point in the "lazy" learning model.
  
	def __init__(self, input, output):
		self.input = input
		self.output = output



class Classifier(object):
  
	def __init__(self, samples):
		self.samples = samples #A list of Sample instances
    
	def neighbors(self, point, k):
		#Finds the k nearest neighbors in self.samples to the input point.
		distances = []
		numParams = len(point)
		for i in xrange(len(self.samples)):
			distance = euclideanDistance(point, self.samples[i].input, numParams)
			distances.append((self.samples[i], distance))
		distances.sort(key = operator.itemgetter(1))
		neighbors = []
		for i in xrange(k):
			neighbors.append(distances[i][0])
		return neighbors
	  
	def voteResponse(self, neighbors):
		#Given a set of possible Sample instances (neighbors), have them vote for an output.
		 votes = {}
		for i in xrange(len(neighbors)):
			response = neighbors[i].output
		if response in votes:
			votes[response] += 1
		else:
			votes[response] = 1
		sortedVotes = sorted(votes.iteritems(), key=operator.itemgetter(1), reverse=True)
		return sortedVotes[0][0]
    
	def classify(self, point, k):
		#Find the output of the classifier for an input point.
		nearest = self.neighbors(point, k)
		result = self.voteResponse(nearest)
		return result
    
	def addSample(self, sample):
		#Add a Sample instance to the current classifier dataset.
		self.samples.append(sample)
