import pygame

class Bird(pygame.sprite.Sprite):

    def __init__(self,displayScreen):

        pygame.sprite.Sprite.__init__(self)

        self.surfaceHeight = displayScreen.get_height()

        self.image = pygame.image.load('img/red.png') # image of bird
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

        self.draw(self.x, self.y) # display bird

    def draw(self,x,y):
        self.screen.blit(self.image, (x,y)) # draw bird over the screen
        self.rect.x, self.rect.y = x,y


    def move(self,input):
        # If bird flapped then jump (i.e. speed upward)
        if input == "FLAP":
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
        self.draw(self.x,self.y)
