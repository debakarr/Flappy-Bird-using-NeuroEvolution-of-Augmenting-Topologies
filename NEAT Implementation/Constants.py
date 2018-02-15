class Constants:
	initialSize = 3 # Initial number of nodes
	bias = 1 # bias
	pipeXDist = 2 # 1st input node
	pipeYDist = 3 # 2nd input node
	output = 20 # output node
	stepSize = 0.1 # step size
	population = 10
	nodeAddingChance = 0.5 # chance of adding any new node
	mutateChance = 0.3 # chance of having mutation. This video is great to know why mutation is important: https://youtu.be/nrKjSeoc7fc
	survivor = 4 # top 4 bird will be selected to make a the new population, based on fitness
