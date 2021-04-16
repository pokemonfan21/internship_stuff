import pygame, random
from bus import Bus
class Street:
  #efine constant values
  SIZE= (800,40)
  SCREEN_DIM = 800,575
  def __init__(self, street_height: int, number_of_buses: int):
    #Street Infromation
    self.rect=pygame.Rect((0,street_height),Street.SIZE)
    self.buses =[]
    #add buses
    self.add_buses(direction, number_of_buses, street_height + 20)

  def add_buses(self, direction: str, number_of_buses: int, street_height: int):
    dp=[]
    for _ in range(number_of_buses):
      while True:
        x_pos = random.randint(30,570)
        valid = True
        for i in range(x_pos-60, x_pos + 60):
          if i in dp:
            valid=False
        if valid:
          dp.append(x_pos)
          break
      self.buses.append(Bus((x_pos, street_height), direction))