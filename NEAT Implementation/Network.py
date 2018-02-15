import math
import random
from Constants import Constants

class Network:
	def __init__(self):
		self.numberOfNodes = Constants.initialSize # Number of initial node (except output)
		self.nodes = [0]*21 # All set to zero (Output node is 20)
		self.edges = [] # empty initally

	# sigmoid function
	def sigmoid(self, x):
		# print('Sigmoid of ', x)
		return 1 / (1 + math.exp(-x))-1

	# Update weight of node. Backpropagation.
	def edgeWeightUpdate(self, start, end):
		for e in self.edges:
			if e['index'] == [start, end]:
				# print('edge weight update')
				e['value'] += random.random()*Constants.stepSize*2 - Constants.stepSize

	# Add edge between two nodes
	def addEdge(self, start, end):
		#print('Add edge')
		self.edges.append({'index':[start, end], 'value':random.random()*2-1})

	# Add node between an edge
	def addNode(self, start, end):
		# print('Add node inbetween')

		self.numberOfNodes += 1	# First increase current node count
		self.edges.append({'index':[start, self.numberOfNodes], 'value': 1}) # edge between starting node and new node
		value = [(l['value'], i) for i, l in enumerate(self.edges) if l['index'] == [start, end]] # get weight of edge and end index
		self.edges.append({'index':[self.numberOfNodes, end], 'value': value[0][0]}) # assign that same weight to new edge
		self.edges.pop(value[0][1]) # delete the previous edge

	# Mutation
	def mutate(self, ):
		# Select random start and end node
		start = math.ceil(random.random()*self.numberOfNodes)
		end = math.ceil(random.random()*(self.numberOfNodes + 1 - Constants.initialSize)) + Constants.initialSize
		# print('start', start)
		# print('end', end)

		# if the random number is greater than number of current nodes, set it to output node
		if end > self.numberOfNodes:
			# print('entered')
			end = Constants.output

		# swap start and end node
		if(start > end):
			start, end = end, start

		# either add a new node or update weight of edge
		if [start, end] in [l['index'] for l in self.edges]:
			if random.random() < Constants.nodeAddingChance:
				self.addNode(start, end)
			else:
				self.edgeWeightUpdate(start, end)

		# else add edge between start and end
		else:
			self.addEdge(start, end)

	def getOutput(self, pipeXDist, pipeYDist):
		# In typical neural network output = f(W1*X1+W2*X2+W3*X3+...+Wn*Xn+b)
		self.nodes[Constants.bias] = 1 # set bias to 1
		self.nodes[Constants.pipeXDist] = pipeXDist*10 # set 1st input
		self.nodes[Constants.pipeYDist] = pipeYDist*10 # set 2nd input
		self.nodes[Constants.output] = 0 # initially set output to zero, bird will not flap

		# for initial case this is not needed. This set all other nodes to zero
		for i in range(Constants.initialSize + 1, self.numberOfNodes +1):
			self.nodes[i] = 0

		# assign value to nodes
		for i in range(1, self.numberOfNodes + 1):
			if i > Constants.initialSize: # if any new node
				self.nodes[i] = self.sigmoid(abs(self.nodes[i]))

			le = [(l['value'], l['index'][1]) for l in self.edges if l['index'][0] == i]
			# print('le: ', le)
			for j in le:
				# This is output of node. Look at the formula at the beginning of getOutput function
				self.nodes[j[1]] += self.nodes[i]*j[0]

		# return output
		return self.nodes[Constants.output]
