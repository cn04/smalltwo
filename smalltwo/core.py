import math

def euclideanDistance(point, point2, length):
  distance = 0
  for i in xrange(length):
    paramDifference = point[i] - point2[i]
    distance += pow(paramDifference, 2)
  return math.sqrt(distance)


class Classifier(object):
  
  def __init__(dataPoints):
    self.dataPoints = dataPoints
    
  def classify(point, k):
    
