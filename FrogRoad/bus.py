import pygame

class Bus(pygame.sprite.Sprite):
  #Define constant value
  LEFT_IMAGE = pygame.image.load('Resources/bus_left.png')
  RIGHT_IMAGE = pygame.image.load('Resources/bus_right.png')
  STARTING_POSITION = (300, 250)
  SIZE = (60,30)
  SCREEN_DIM=800,575
  MOVE_DIST=2

  #create a Log object
  def __init__(self,starting_position: turple,direction: str):
    #sprite Information
    super().__init__()
    self.image = Bus.LEFT_IMAGE if direction == 'Left' else Bus.RIGHT_IMAGE
    # Bus infromation
    self.rect = pygame.Rect((0,0),Bus.SIZE)
    self.rect.center=Bus.STARTING_POSITION
    self.direction = direction
  def move(self):
    if self.direction=='Left':
      self.rect.centerx-=Bus.MOVE_DIST
      #Car moves off screen
      if self.rect.right <= 0:
        self.rect.centerx= Bus.SCREEN_DIM[0]+(Bus.SIZE[0]/2)
    else:
      self.rect.centerx+=Bus.MOVE_DIST
      if self.rect.left >= Bus.SCREEN_DIM[0]:
        self.rect.centerx-=(Bus.SIZE[0]/2)

