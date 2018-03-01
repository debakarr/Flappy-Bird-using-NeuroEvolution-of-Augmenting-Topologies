from Bird import Bird
from Constants import Constants
import math
import random

class Generation:
	def __init__(self, surface):
		self.generationNum = 1 # initial generation
		self.birds = [] # 
		for i in range(0, Constants.population): # Genration 1
			# print('Creating GEN 1...')
			self.birds.append(Bird(surface))
			self.birds[i].network.mutate()
		self.alive = Constants.population # Set alive count to initial population
		self.surface = surface # screen

	# New generation is made based on the top fittest birds
	# this is used for creating breed
	def newBreed(self, bird1, bird2):
		child = Bird(self.surface)

		# This section also need some improvement. For now this just take the best bird available.

		# Select the best out of the two parent or to say Survival of the fittest.
		if(self.birds[bird1].fitness < self.birds[bird2].fitness):
			self.birds[bird1], self.birds[bird2] = self.birds[bird2], self.birds[bird1]

		# Set the initial number of nodes for the child as the number of node of the fittest parent
		child.network.numberOfNodes = self.birds[bird1].network.numberOfNodes

		# in Constant we have set the index of initial node(bias) as 1
		# this loop just set the value of each node of child to that of the parent
		for i in range(1, child.network.numberOfNodes + 1):
			value1 = [(l['value'], l['index'])  for l in self.birds[bird1].network.edges if l['index'][0] == i]
			value2 = [(l['value'], l['index'])  for l in self.birds[bird2].network.edges if l['index'][0] == i]

			if(len(value2)>0):
				value = value2 if random.random() <= 0.5 else value1

				''' Uncomment this for debug output
				file = open('text.txt', 'a')
				file.write("\nvalue1: " + str(value1))
				file.write("\nvalue2:"+ str(value2))
				file.write("\nvalue:"+ str(value))
				file.write("\n\n==========================\n\n")
				file.close()
				'''
				
				for l in value:
					child.network.edges.append({'index':[i, value[0][1][1]], 'value':value[0][0]})
			else:
				for l in value1:
					child.network.edges.append({'index':[i, value1[0][1][1]], 'value':value1[0][0]})

		# This is for mutation
		if random.random() <= Constants.mutateChance:
			child.network.mutate()

		# setting child color yellow 
		child.setImage('../img/yellow.png')

		# return the new child
		return child		

	# function to sort the bird according to thier fitness
	def sortBird(self):
		self.birds = sorted(self.birds, key=lambda bird: bird.fitness, reverse=True) # reverse = True i.e. decending

	# function create new generation
	def nextGen(self):
		self.sortBird() # sort according to fitness

		'''
		for bird in self.birds:
			print(bird.fitness)
		'''

		# kill all bird except the top fittest one.
		for i in range(len(self.birds)- Constants.survivor):
			self.birds.pop()

		# add new vacant place in the popuation after breeding
		for i in range(len(self.birds), 11):
			self.birds.append(self.newBreed(math.floor(random.random()*Constants.survivor), math.floor(random.random()*Constants.survivor)))

		# increament generation count
		self.generationNum += 1

		# return bird as well as generation count
		return self.birds, self.generationNum
