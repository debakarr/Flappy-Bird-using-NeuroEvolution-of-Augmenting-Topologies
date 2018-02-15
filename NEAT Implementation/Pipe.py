import pygame
import numpy as np

# set the pipe normal or upside-down (use only 1 image of pipe to create two views)
class PipeBlock(pygame.sprite.Sprite):

	def __init__(self,image,upper):

		pygame.sprite.Sprite.__init__(self)

		if upper == False:
			self.image = pygame.image.load(image)
		else:
			self.image = pygame.transform.rotate(pygame.image.load(image),180)

		self.rect = self.image.get_rect()


# Pipe class
class Pipe(pygame.sprite.Sprite):
	
	
	def __init__(self,screen,x):

		pygame.sprite.Sprite.__init__(self)

		self.screen = screen # surface/screen
		self.lowerBlock = PipeBlock('../img/pipe.png',False) # pipe image defualt
		self.upperBlock = PipeBlock('../img/pipe.png',True) # pipe image rotated upside-down
		self.gapBetweenPipes  = 100 # gaps between pipe
		self.surfaceWidth = screen.get_width() # screen width

		self.pipeWidth = self.upperBlock.rect.width
		self.x = x # initial pipe position
		

		heights = self.getHeight() # height
		self.upperY, self.lowerY = heights[0], heights[1]

		self.behindBird = 0 # by default pipe is ahead of bird
		self.draw() # draw over screen


	def getHeight(self):

		randVal = int(np.random.normal(5, 1, 1))

		midYPos = 106 + 30*randVal

		upperPos = midYPos - (self.gapBetweenPipes/2)
		lowerPos = midYPos + (self.gapBetweenPipes/2)

		return([upperPos,lowerPos])

	def draw(self):

		self.screen.blit(self.lowerBlock.image, (self.x, self.lowerY))
		self.screen.blit(self.upperBlock.image, (self.x, self.upperY - self.upperBlock.rect.height))
		self.upperBlock.rect.x, self.upperBlock.rect.y = self.x, (self.upperY - self.upperBlock.rect.height)
		self.lowerBlock.rect.x, self.lowerBlock.rect.y = self.x, self.lowerY

	def move(self):

		self.x -= 3

		if self.x <= 0:
			self.x = self.surfaceWidth
			heights = self.getHeight()
			self.upperY, self.lowerY = heights[0], heights[1]
			self.behindBird = 0

		self.draw()
		return([self.x+(self.pipeWidth/2), self.upperY, self.lowerY])

	# setting position of pipe
	def setPos(self, x):
		self.x = x
		heights = self.getHeight() # height
		self.upperY, self.lowerY = heights[0], heights[1]