import pygame
from pygame.locals import *
import sys
import time
from Bird import Bird
from Pipe import Pipe
import random
import math

framesPerSecond = 40 # Set framesPerSecond of the game
surfaceWidth  = 286 # width of the screen
surfaceHeight = 509 # height of the screen
score = 0 # Initial score
background = pygame.image.load('../img/day.png') # Background image
# gameover = 0

# If game over
def gameOver(surface, clock):
	# set global score to 0
	global score, background
	score = 0

	backgroundChoice = ['../img/day.png', '../img/night.png']
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

def topDisplay(surface, score, distance, birdCord, gapCord):
	smallText = pygame.font.SysFont(None, 20)
	scoreDisplay = smallText.render("Score: " + str(score), True, (255, 255, 255))
	distanceDisplay = smallText.render("Distance: " + str(distance), True, (255, 255, 255))
	bCord = smallText.render("Bird Coord: " + str(birdCord[0]) + ", " + str(birdCord[1]), True, (255, 255, 255))
	gCord = smallText.render("Gap Coord: " + str(gapCord[0]) + ", " + str(gapCord[1]), True, (255, 255, 255))
	fitness = smallText.render("Fitness: " + str(math.ceil(calcFitness(score, distance, birdCord, gapCord))), True, (255, 255, 255))
	surface.blit(scoreDisplay, [0, 0])
	surface.blit(distanceDisplay, [0, 20])
	surface.blit(bCord, [0, 40])
	surface.blit(gCord, [0, 60])
	surface.blit(fitness, [0, 80])
	# surface.blit(gCord, [0, 80])
	# calcFitness(score, distance, birdCord, gapCord)
	# print("score: ", type(int(str(score))))
	# print("distance: ", type(int(str(distance))))

def calcFitness(score, distance, birdCord, gapCord):
	try:
		birdAndGapDist = math.sqrt((gapCord[0]-birdCord[0])**2 + (gapCord[1] - birdCord[1]))
	except:
		birdAndGapDist = 0.001
	fitness = (score*2) + (distance*2) + ((1/birdAndGapDist))

	return fitness


def game():
	# main game part

	# Initialization
	pygame.init()

	# Creating objects
	clock = pygame.time.Clock()
	surface  = pygame.display.set_mode((surfaceWidth, surfaceHeight))
	pygame.display.set_caption('Flappy Bird')

	# Setting score as global variable
	global score

	# Declaring bird 
	flappyBird = Bird(surface)
	firstPipe = Pipe(surface, surfaceWidth+100)
	secondPipe = Pipe(surface, surfaceWidth+250)

	# Grouping pipes
	pipeGroup = pygame.sprite.Group()
	pipeGroup.add(firstPipe.upperBlock)
	pipeGroup.add(secondPipe.upperBlock)
	pipeGroup.add(firstPipe.lowerBlock)
	pipeGroup.add(secondPipe.lowerBlock)

	moved = False
	pause = 0

	# Whole game machenism
	while True:

		# draw over the background
		surface.blit(background,(0,0))

		# check if bird and pipes are colliding
		t = pygame.sprite.spritecollideany(flappyBird,pipeGroup)

		# check if the bird is toching the screen top or bottom 
		if t!=None or (flappyBird.y == 509 - flappyBird.height) or (flappyBird.y == 0):
			# if yes the it's game over
			print("GAME OVER")
			print("FINAL SCORE IS %d"%score)
			gameOver(surface, clock)
		
		# else check for any event (eg. button pressed)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_w or event.key == K_UP):
				flappyBird.move("FLAP")
				moved = True		

		if moved == False:
			flappyBird.move(None)
		else:
			moved = False

		
		pipe1Pos = firstPipe.move()
		if pipe1Pos[0] <= int(surfaceWidth * 0.2) - int(flappyBird.rect.width/2):
			if firstPipe.behindBird == 0:
				firstPipe.behindBird = 1
				score += 1
				print("SCORE IS %d"%score)

		pipe2Pos = secondPipe.move()
		if pipe2Pos[0] <= int(surfaceWidth * 0.2) - int(flappyBird.rect.width/2):
			if secondPipe.behindBird == 0:
				secondPipe.behindBird = 1
				score += 1
				print("SCORE IS %d"%score)

		birdCord = [flappyBird.x, flappyBird.y]
		closestPipe = pipe1Pos if (pipe1Pos[0]<pipe2Pos[0]) else pipe2Pos
		gapCord = [closestPipe[0], ((closestPipe[1] + closestPipe[2])/2)]

		topDisplay(surface, score, flappyBird.distance, birdCord, gapCord)
		
		

		if pause==0:
			pygame.display.update()
		else:
			pygame.time.wait(1000)

		clock.tick(framesPerSecond)

game()