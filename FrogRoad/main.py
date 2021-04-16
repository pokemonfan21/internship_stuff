import pygame, random
from frog import Frog
from log import Logs
from street import Street
#Initialize Pygame's internal variables
pygame.init()

#Only allows KEYDOWN and QUIT events
pygame.event.set_allowed([pygame.KEYDOWN,pygame.QUIT])

#Initialize a window with the screen size defiend
SCREEN_DIM= WIDTH, HEIGHT=800,575
SCREEN = pygame.display.set_mode(SCREEN_DIM)
#Renames the window
pygame.display.set_caption('Frog Road')
#define's a Clock object to control the game's frame rate
CLOCK = pygame.time.Clock()
FPS = 60

#RGB Values
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (94,221,95)
YELLOW = (100,85,0)
BROWN = (118, 92, 72)
GRAY=(175,175,175)
#Create Frog object
frog = Frog()
#Create log object
log = Log()
#Create log object
streets=[]
number_of_buses=3
street_height=400
for _ in range(2):
  streets.append(Street(street_height,'Left',random.randint(1, number_of_buses)))
  streets.append(Street(street_height-40,'Right',random.randint(1, number_of_buses)))
  street_height-=80

#Game Loop
while True:
  # Tick forward at 60 frames per second
  CLOCK.tick(FPS)
  
  #Event listener:Listens for an input the player provides
  for event in pygame.event.get():
    #User closes
    if event.type==pygame.QUIT:
      sys.exit()
      #User presses a key
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_w: #w
          frog.move_up()
      if event.key==pygame.K_a: #a
          frog.move_left()
      if event.key==pygame.K_s: #s
          frog.move_down()
      if event.key==pygame.K_d: #d
          frog.move_right()
  #Move Log
  log.move()

  if frog.rect.colliderect(log.rect):
    frog.move_on_log(log)
  #Make background a soild color
  SCREEN.fill(BLACK)
  for street in streets:
    SCREEN.fill(GRAY, street.rect)
    #buses
    for bus in street.buses:
      #Draw bus
      SCREEN.blit(bus.image, bus.rect)
      bus.move()
      if frog.rect.colliderect(bus.rect):
        frog.reset_position()
  # Code for the game will be here
  
  #Draw frog
  SCREEN.blit(frog.image, frog.rect)
  #Draw log
  SCREEN.blit(log.image, log.rect)
  
  #Update the screen
  pygame.display.flip()