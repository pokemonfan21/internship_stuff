import pygame
from log import Log
class Frog(pygame.sprite.Sprite):
  #Define constant value
  IMAGE = pygame.image.load('Resources/frog.png')
  STARTING_POSITION = (400, 480)
  SIZE = (20,10)
  SCREEN_DIM=800,575
  MOVE_DIST=10
  #create a frog object
  def __init__(self):
    #sprite Information
    super().__init__()
    self.image = Frog.IMAGE
    # Frog infromation
    self.rect = pygame.Rect((0,0),Frog.SIZE)
    self.rect.center=Frog.STARTING_POSITION
    self.lives = 3
  def move_up(self):
    if self.rect.top >= 20:
      self.rect.centery-= Frog.MOVE_DIST

  def move_down(self):
    if self.rect.bottom<= Frog.SCREEN_DIM[1]-20:
      self.rect.centery += Frog.MOVE_DIST
  def move_left(self):
    if self.rect.left >= 20:
      self.rect.centerx -= Frog.MOVE_DIST
  def move_right(self):
    if self.rect.right<= Frog.SCREEN_DIM[0]-20:
      self.rect.centerx += Frog.MOVE_DIST
  def reset_position(self):
    self.rect.center=Frog.STARTING_POSITION
    self.lives-=1
  def move_on_log(self,log:Log):
    self.rect.centerx+=Log.MOVE_DIST
    if self.rect.left >= Log.SCREEN_DIM[0]:
      diff=log.rect.right-self.rect.centerx
      self.rect.centerx = -diff