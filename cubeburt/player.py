import pygame
from game_board import Board

class Player(pygame.sprite.Sprite):
    # Define constant values
    RIGHT_IMAGE = pygame.image.load('resources/player_right.png')
    LEFT_IMAGE = pygame.image.load('resources/player_left.png')
    SIZE = 20, 40
    SCREEN_DIM = 600, 50
    STARTING_PLATFORM = Board.BOARD[0][0]

    def __init__(self):
        # Graphic information
        super().__init__()
        self.image = Player.RIGHT_IMAGE
        # Character information
        self.current_platform = Player.STARTING_PLATFORM
        self.size = (20, 40)
        self.rect = pygame.Rect((0,0), Player.SIZE)
        self.rect.center = self.current_platform.rect.center 
        self.lives = 3  

    '''
    Note About All Move Functions
    Returns True while still animating
    Returns False when animation is over
    '''
    
    def move_up(self) -> bool:
        # Try to move Player up
        try:
            # Create a List IndexError if current_platform.row is 0 because Python allows negative indexes
            if self.current_platform.row == 0:
                raise IndexError

            next_platform = Board.BOARD[self.current_platform.row - 1][self.current_platform.col]
            # Animate Player up until on next_platform
            if self.rect.centery != next_platform.rect.centery:
                self.rect.centery -= 1
                return True

            # Update current_platform to Platform above
            self.current_platform = next_platform
            self.current_platform.activated = True
            return False

        # List IndexError happens if there is no Platform above
        except IndexError:
            # Animate into the void 55 pixels
            if self.rect.centery != self.current_platform.rect.centery - 55:
                self.rect.centery -= 1
                return True
            # Reset Player
            self.reset()
            return False
                  
    def move_down(self):
        # Try to move Player down
        try:
            next_platform = Board.BOARD[self.current_platform.row + 1][self.current_platform.col]
            # Animate Player down until on next_platform
            if self.rect.centery != next_platform.rect.centery:
                self.rect.centery += 1
                return True

            # Update current_platform to Platform below
            self.current_platform = next_platform
            self.current_platform.activated = True
            return False

        # List IndexError happens if there is no Platform below
        except IndexError:
            # Animate into the void 55 pixels
            if self.rect.centery != self.current_platform.rect.centery + 55:
                self.rect.centery += 1
                return True
            # Reset Player
            self.reset()
            return False

    def move_left(self):
        self.image = Player.LEFT_IMAGE
        # Try to move Player left
        try:
            # Create a List IndexError if current_platform.col is 0 because Python allows negative indexes
            if self.current_platform.col == 0:
                raise IndexError

            next_platform = Board.BOARD[self.current_platform.row][self.current_platform.col - 1]
            # Animate Player left until on next_platform
            if self.rect.centerx != next_platform.rect.centerx:
                self.rect.centerx -= 1
                return True

            # Update current_platform to Platform to the left
            self.current_platform = next_platform
            self.current_platform.activated = True
            return False

        # List IndexError happens if there is no Platform to the left
        except IndexError:
            # Animate into the void 55 pixels
            if self.rect.centerx != self.current_platform.rect.centerx - 55:
                self.rect.centerx -= 1
                return True
            # Reset Player
            self.reset()
            return False
    
    def move_right(self):
        self.image = Player.RIGHT_IMAGE
        # Try to move Player right
        try:
            next_platform = Board.BOARD[self.current_platform.row][self.current_platform.col + 1]
            # Animate Player right until on next_platform
            if self.rect.centerx != next_platform.rect.centerx:
                self.rect.centerx += 1
                return True

            # Update current_platform to Platform to the right
            self.current_platform = next_platform
            self.current_platform.activated = True
            return False

        # List IndexError happens if there is no Platform to the right
        except IndexError:
            # Animate into the void 55 pixels
            if self.rect.centerx != self.current_platform.rect.centerx + 55:
                self.rect.centerx += 1
                return True
            # Reset Player
            self.reset()
            return False

    def reset(self):
        self.current_platform = Player.STARTING_PLATFORM
        self.rect.center = self.current_platform.rect.center
        self.lives -= 1