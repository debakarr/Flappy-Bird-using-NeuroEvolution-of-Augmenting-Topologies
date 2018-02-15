import pygame
from Network import Network

class Bird(pygame.sprite.Sprite):

    def __init__(self,displayScreen):
    	# Call the Sprite constructor (parent class constructor)
        pygame.sprite.Sprite.__init__(self)

        # Surface Height
        self.surfaceHeight = displayScreen.get_height()
        # image of bird
        self.image = pygame.image.load('../img/red.png')
        # setting initial position of bird
        self.x = 40
        self.y = self.surfaceHeight/2
        
        self.rect = self.image.get_rect() # area of the image
        self.height = self.rect.height # height of the image
        self.screen = displayScreen # getting surface
        
        self.normalSpeed = -9 # speed while flapped Up
        self.moveDownSpeed = 10 # Normal decending speed
        self.moveDownAcceleration = 1 # Deaccelaration
        self.moveUp = -9 # Acceleration upward
        self.isFlapped = False # Did the bird flapped?
        self.distance = 0 # Hold total distance covered by the bird
        self.network = Network() # Each bird has it's own neural network
        self.fitness = 0 # Fitness value
        self.isAlive = True # check whether the bird is alive or not

        self.draw(self.x, self.y) # display bird

    def draw(self,x,y):
        self.screen.blit(self.image, (x,y)) # draw bird over the screen
        self.rect.x, self.rect.y = x,y


    def move(self,pipeXDist, pipeYDist):

        # There are two input to the neural network
        # Input 1 - distance of the bird from the mid point of the gap in x-axis
        # Input 2 - distance of the bird from the mid point of the gap in y-axis

        # Check if the bird is alive or not, if alive then jump based on the output of the neural network
        if self.isAlive:
            output = self.network.getOutput(pipeXDist, pipeYDist) # Output of neural network
            # print(output)
            # flap if output is greater then 0
            if output > 0:
                # print('Jump')
                self.normalSpeed = self.moveUp
                self.isFlapped = True

        # If nothing is pressed then decend
        if self.normalSpeed < self.moveDownSpeed and not self.isFlapped:
            self.normalSpeed += self.moveDownAcceleration

        # reset isFlapped
        if self.isFlapped:
            self.isFlapped = False

        # calculate the location and redraw the bird
        self.y += min(self.normalSpeed, self.surfaceHeight - self.y - self.height)
        self.y = max(self.y,0)
        self.distance += 1
        self.draw(self.x,self.y)

    def setImage(self, image):
        self.image = pygame.image.load(image)
