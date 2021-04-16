import pygame

class Log(pygame.sprite.Sprite):
  #Define constant value
  IMAGE = pygame.image.load('Resources/log.png')
  STARTING_POSITION = (300, 150)
  SIZE = (60,30)
  SCREEN_DIM=800,575
  MOVE_DIST=1

  #create a Log object
  def __init__(self):
    #sprite Information
    super().__init__()
    self.image = Log.IMAGE

    # Log infromation
    self.rect = pygame.Rect((0,0),Log.SIZE)
    self.rect.center=Log.STARTING_POSITION
  def move(self):
    self.rect.centerx+=Log.MOVE_DIST
    #Car moves off screen
    if self.rect.left >= Log.SCREEN_DIM[0]:
      self.rect.centerx= -Log.SIZE[0] / 2

