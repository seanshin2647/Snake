# A file for all of the classes I will be using.

from import_libraries import *

# I plan on having two classes make up the human player,
# one for the head and one for the snake sections.
class Player_Head(pygame.sprite.Sprite):
    def __init__(self, board_width, board_height):
        super().__init__()

        self.side_length = 30

        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(SILVER)
        self.rect = self.image.get_rect()

        self.rect.x = board_width * 0.1

        self.initial_y = random.randrange((0 + (self.side_length * 4)), 
            (board_height - (self.side_length * 3)))
        self.rect.y = (int(self.initial_y / self.side_length)) * self.side_length

    # I added future_movement to differentiate how I calculate the head's rectangular position handling.
    def gridset_x(self, future_movement):
        self.rect.x = (int((self.rect.x + future_movement) / self.side_length)) * self.side_length

    def gridset_y(self, future_movement):
        self.rect.y = (int((self.rect.y + future_movement) / self.side_length)) * self.side_length

# TODO: Make this independent. Not a child.
class Body(pygame.sprite.Sprite):
    # ahead_x and ahead_y are the x and y of the body part right in front.
    def __init__(self, chain_order, locations_length):
        super().__init__()
        
        # This is the index value where the body will get its location from.
        self.location = locations_length - (chain_order * 6)

        self.side_length = 30

        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

class Apple(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height):
        super().__init__()

        self.side_length = 30

        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.initial_x = random.randrange(1, (display_width - self.side_length))
        # This gives us the row the apple will be in instead of the raw coordinates.
        self.rect.x = (int(self.initial_x / self.side_length)) * self.side_length

        self.initial_y = random.randrange(1, (display_height - self.side_length))
        # This gives us the column the apple will be in instead of the raw coordinates.
        self.rect.y = (int(self.initial_x / self.side_length)) * self.side_length
