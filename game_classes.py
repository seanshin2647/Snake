# A file for all of the classes I will be using.

from import_libraries import *

# I plan on having two classes make up the human player,
# one for the head and one for the snake sections.
class Player_Head(pygame.sprite.Sprite):
    def __init__(self, board_width, board_height):
        super().__init__()

        self.side_length = 20

        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        self.rect.x = board_width * 0.1

        self.initial_y = random.randrange((0 + (self.side_length * 4)), 
            (board_height - (self.side_length * 3)))
        self.rect.y = (int(self.initial_y / 20)) * 20

    # I added future_movement to differentiate how I calculate the head's rectangular position handling.
    def gridset_x(self, future_movement):
        self.rect.x = (int((self.rect.x + future_movement) / 20)) * 20

    def gridset_y(self, future_movement):
        self.rect.y = (int((self.rect.y + future_movement) / 20)) * 20

    def move(self, x_movement, y_movement):
        self.rect.x += x_movement
        self.rect.y += y_movement

# TODO: Make this independent. Not a child.
class Body(Player_Head):
    # ahead_x and ahead_y are the x and y of the body part right in front.
    def __init__(self, ahead_x, ahead_y, display_width, display_height):
        super().__init__(display_width, display_height)

        self.rect.x = (ahead_x - (self.side_length + 10))
        self.rect.y = (ahead_y - (self.side_length + 10))

class Apple(pygame.sprite.Sprite):
    def __init__(self, display_width, display_height):
        super().__init__()

        self.side_length = 20

        self.image = pygame.Surface([self.side_length, self.side_length])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.initial_x = random.randrange(1, (display_width - self.side_length))
        # This gives us the row the apple will be in instead of the raw coordinates.
        self.rect.x = (int(self.initial_x / 20)) * 20

        self.initial_y = random.randrange(1, (display_height - self.side_length))
        # This gives us the column the apple will be in instead of the raw coordinates.
        self.rect.y = (int(self.initial_x / 20)) * 20
