import pygame, sys
from game_board import Board
from player import Player

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("JUMPBERT!")

CLOCK = pygame.time.Clock()
FPS=60

BLACK=(0,0,0)
WHITE= (255,255,255)
ORANGE=(255,87,51)
YELLOW =(255,255,0)

player = Player()
player_animating=[False,False,False,False]
while True:
  CLOCK.tick(FPS)

   # Event listener: Listens for an input the player provides
  for event in pygame.event.get():
    # User closes the game window
    if event.type == pygame.QUIT:
        sys.exit()
    # User presses a key
    if event.type == pygame.KEYDOWN:
        # Not animating in any direction
        if not True in player_animating:
            if event.key == pygame.K_w: # W
                player_animating[0] = True
            if event.key == pygame.K_a: # A
                player_animating[2] = True
            if event.key == pygame.K_s: # S
                player_animating[1] = True
            if event.key == pygame.K_d: # D
                player_animating[3] = True

  # Animate player
  if player_animating[0]:
      player_animating[0] = player.move_up()
  if player_animating[1]:
      player_animating[1] = player.move_down()
  if player_animating[2]:
      player_animating[2] = player.move_left()
  if player_animating[3]:
      player_animating[3] = player.move_right()
        
  SCREEN.fill(BLACK)

  for row in Board.BOARD:
    for platform in row:
      if platform.activated:
        SCREEN.fill(YELLOW,platform.rect)
      else:
        SCREEN.fill(ORANGE,platform.rect)
  SCREEN.blit(player.image, player.rect)
  pygame.display.flip()