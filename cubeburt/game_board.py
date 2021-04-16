import pygame
class Platform:
  #Defied constant values
  BORDER= 5
  SIZE=50,50
  SCREEN_DIM=600,500

  def __init__(self,row: int, col: int):
    #platform info
    self.rect=pygame.Rect((0,0), Platform.SIZE)
    self.rect.centerx=((Platform.SIZE[0]+Platform.BORDER)* col)
    self.rect.centery=((Platform.SIZE[1]+Platform.BORDER)* row)
    self.col=col
    self.row=row 
    self.activated=False    

class Board:
  BOARD = [
        [Platform(0, 0)],
        [Platform(1, 0), Platform(1, 1)],
        [Platform(2, 0), Platform(2, 1), Platform(2, 2)],
        [Platform(3, 0), Platform(3, 1), Platform(3, 2), Platform(3, 3)],
        [Platform(4, 0), Platform(4, 1), Platform(4, 2), Platform(4, 3), Platform(4, 4)],
        [Platform(5, 0), Platform(5, 1), Platform(5, 2), Platform(5, 3), Platform(5, 4), Platform(5, 5)],
        [Platform(6, 0), Platform(6, 1), Platform(6, 2), Platform(6, 3), Platform(6, 4), Platform(6, 5), Platform(6, 6)]
    ]
