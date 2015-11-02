import math
import operator


def euclideanDistance(firstPoint, secondPoint, length):
  distance = 0
  for i in xrange(length):
    paramDifference = firstPoint[i] - secondPoint[i]
    distance += pow(paramDifference, 2)
  return math.sqrt(distance)
  
  

class Sample(object):
  
  def __init__(self, input, output):
    self.input = input
    self.output = output



class Classifier(object):
  
  def __init__(self, samples):
    self.samples = samples
    
  def neighbors(self, point, k):
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
    nearest = self.neighbors(point, k)
    result = self.voteResponse(nearest)
    return result
    
  def addSample(self, sample):
	  self.samples.append(sample)
