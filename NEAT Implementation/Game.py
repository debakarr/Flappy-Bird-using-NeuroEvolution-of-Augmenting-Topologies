import pygame
from pygame.locals import *
import sys
import time
from Bird import Bird
from Pipe import Pipe
import random
import math
from GeneticAlgorithm import Generation

framesPerSecond = 30 # Set framesPerSecond of the game
surfaceWidth  = 286 # width of the screen
surfaceHeight = 509 # height of the screen
score = 0 # Initial score
background = pygame.image.load('../img/day.png') # Background image
# gameover = 0
surface  = pygame.display.set_mode((surfaceWidth, surfaceHeight)) # surface/screen
birds = Generation(surface) # 1st Genration of Birds

'''
# If game over
def gameOver(surface, clock):
	# set global score to 0
	global score, background
	score = 0

	backgroundChoice = ['img/day.png', 'img/night.png']
	background = pygame.image.load(random.choice(backgroundChoice)) # Background image

	#display message 'Game Over!'
	msgSurface(surface, clock, 'Game Over!')

def msgSurface(surface, clock, text):
	# Set font for game over message 
	# (still using system font as I am facing some permission error and still need to figure out that how to get around of that permission)
	smallText = pygame.font.SysFont(None, 30)
	largeText = pygame.font.SysFont(None, 50)

	# makeTextObject is a function used to render text on screen
	titleTextSurf, titleTextRect = makeTextObject(text, largeText)
	titleTextRect.center = surfaceWidth/2, surfaceHeight/2
	surface.blit(titleTextSurf, titleTextRect)

	typicalTextSurface, typicalTextRect = makeTextObject('Press any key to continue...', smallText)
	typicalTextRect.center = surfaceWidth/2, ((surfaceHeight/2)+100)
	surface.blit(typicalTextSurface, typicalTextRect)

	# Updating screen
	pygame.display.update()
	time.sleep(1) # Making sure the message screen does not disappear instantly

	# Hold the screen
	while replay_or_quit() == None:
		clock.tick()

	# Replay the game
	game()

# Render text message
def makeTextObject(text, font):
	textSurface = font.render(text, True, (255,0,0))
	return textSurface, textSurface.get_rect()

# Check whether user pressed any key
def replay_or_quit():
	for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
		if event.type == pygame.QUIT: #quit if game is closed
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			continue
		return event.key

	# keep on returning null and in msgSurface we are holding the frame
	return None
'''

# Display on top left
def topDisplay(surface, score, distance, birdCord, gapCord, genrationCount):
	global framesPerSecond # using global FPS variable

	# Using system font for now to display things like Gneration, Score, Distance, etc.
	smallText = pygame.font.SysFont(None, 25)
	generation = smallText.render("Generation:" + str(genrationCount), True, (255, 255, 255))
	scoreDisplay = smallText.render("Best Score:" + str(score), True, (255, 255, 255))
	distanceDisplay = smallText.render("Best Distance:" + str(distance), True, (255, 255, 255))
	frames = smallText.render("Frames:" + str(framesPerSecond), True, (255, 255, 255))
	# bCord = smallText.render("Bird Coord:" + str(birdCord[0]) + ", " + str(birdCord[1]), True, (255, 255, 255))
	# gCord = smallText.render("Gap Coord:" + str(gapCord[0]) + ", " + str(gapCord[1]), True, (255, 255, 255))
	fitness = smallText.render("Best Fitness:" + str(math.ceil(calcFitness(score, distance, birdCord, gapCord)/100)), True, (255, 255, 255))
	surface.blit(generation, [0, 0])
	surface.blit(scoreDisplay, [0, 20])
	surface.blit(distanceDisplay, [0, 40])
	# surface.blit(bCord, [0, 60])
	# surface.blit(gCord, [0, 80])
	surface.blit(fitness, [0, 60])
	surface.blit(frames, [0, 80])
	# surface.blit(gCord, [0, 80])
	# calcFitness(score, distance, birdCord, gapCord)
	# print("score: ", type(int(str(score))))
	# print("distance: ", type(int(str(distance))))

# Calcuating fitness based on 3 main features
# 1st: Score of the bird (number of pipes crossed)
# 2nd: Total distance covered
# 3rd: distance between the bird and mid point of pipe gap
def calcFitness(score, distance, birdCord, gapCord):
	# There is a problem. If the bird cross path exactly from the middle of the gap then for that momment
	# the distance between the bird and the gap will be 0
	# Which actually make 1/(Bird and Gap distance) undefined
	# Also getting negative values sometime, which make sqrt(value) undefined
	# So putting a try-except statement for now
	try:
		birdAndGapDist = math.sqrt((gapCord[0]-birdCord[0])**2 + (gapCord[1] - birdCord[1])**2)
	except:
		birdAndGapDist = 0.001
	fitness = (score*2) + (distance*200) + ((1/birdAndGapDist)) # calculating fitness
	return fitness # returning fitness


def game(surface):
	# Main game part

	# Initialization
	pygame.init()

	# Creating objects
	clock = pygame.time.Clock()
	pygame.display.set_caption('Flappy Bird')

	# Setting score as global variable
	global score

	# Declaring pipe objects	
	firstPipe = Pipe(surface, surfaceWidth+30)
	secondPipe = Pipe(surface, surfaceWidth+180)

	# Grouping pipes
	pipeGroup = pygame.sprite.Group()
	pipeGroup.add(firstPipe.upperBlock)
	pipeGroup.add(secondPipe.upperBlock)
	pipeGroup.add(firstPipe.lowerBlock)
	pipeGroup.add(secondPipe.lowerBlock)

	# setting some variabe to make the game mechanism work
	isAlive = 10
	moved = False
	pause = 0
	genrationCount = 1
	pipe1Pos = [0, 0, 0]
	pipe2Pos = [0, 0, 0]
	global framesPerSecond

	# Whole game mechanism
	while True:
		# draw over the background
		surface.blit(background,(0,0))			
		
		# Check
		for event in pygame.event.get(): # if close button is pressed
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == KEYDOWN and (event.key == K_i): # if '+' is pressed, if yes increase speed
				framesPerSecond *= 2
			if event.type == KEYDOWN and (event.key == K_d):
				framesPerSecond /= 2
		
		'''
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_w or event.key == K_UP):
				flappyBird.move("FLAP")
				moved = True		

		if moved == False:
			flappyBird.move(None)
		else:
			moved = False
		'''	

		''' Uncomment this for debug output
		birdCount = 1
		print("=====================================================")
		'''

		# Check if birds and pipes are colliding
		# This part is unoptimized right now. This could be improved more.
		for bird in birds.birds: # Loop through all birds
			colide = (pygame.sprite.spritecollideany(bird,pipeGroup)) # Check if collide

			''' Uncomment this for debug output
			print("Generation: ", genrationCount)
			print("Nodes:", bird.network.nodes)
			print("Edges:", bird.network.edges)
			print("Bird No.:", birdCount)
			print()

			birdCount += 1

			if birdCount == 10:
				birdCount = 1
			'''

			if colide != None or (bird.y == 509 - bird.height) or (bird.y == 0): # if collide or touch the top or bottom of the screen
				bird.isAlive = False # set isAlive attribute to False
				isAlive -= 1 # decrement isAlive count
				score = 0 # set score back to 0.
				bird.distance = 0 # set distance covered by bird to zero 
			if isAlive == 0: # if no bird is alive
				# surface.blit(background,(0,0))
				# time.sleep(5)
				# game(surface)
				isAlive = 10 # reset counter
				firstPipe.setPos(surfaceWidth+30)
				secondPipe.setPos(surfaceWidth+180)
				_, genrationCount = birds.nextGen() # make new genration

			birdCord = [bird.x, bird.y] # getting coordinates of bird
			closestPipe = pipe1Pos if (pipe1Pos[0]<pipe2Pos[0]) else pipe2Pos # getting closest pipe 
			# (closest because 2 pipe are draw at the same time on screen)
			gapCord = [closestPipe[0], ((closestPipe[1] + closestPipe[2])/2)] # getting mid point of the gap
			bird.fitness = calcFitness(score, bird.distance, birdCord, gapCord) # calculating fitness
			bird.move(gapCord[0]-birdCord[0], gapCord[1]-birdCord[1]) # move the bird. NOTE: Here the two parameter are send as input of neural network


		birds.sortBird() # Sort bird. This is done to just take the fittest one and based on that increment the score

		pipe1Pos = firstPipe.move() # Move the first pipe
		if pipe1Pos[0] <= int(surfaceWidth * 0.2) - int(birds.birds[0].rect.width/2): # Compairing if the bird crossed the pipe
			if firstPipe.behindBird == 0:
				firstPipe.behindBird = 1
				score += 1 # incrementing score
				print("Current Score:", score) # print score to console

		# Doin g the exact same thing with 2nd pipe
		pipe2Pos = secondPipe.move()
		if pipe2Pos[0] <= int(surfaceWidth * 0.2) - int(birds.birds[0].rect.width/2):
			if secondPipe.behindBird == 0:
				secondPipe.behindBird = 1
				score += 1
				print("Current Score:", score)
		
		# Display details
		topDisplay(surface, score, birds.birds[0].distance, birdCord, gapCord, genrationCount)


		# This part is still not implemented
		if pause==0:
			pygame.display.update()
		else:
			pygame.time.wait(1000)

		# setting FPS
		clock.tick(framesPerSecond)

# calling game
game(surface)