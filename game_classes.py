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
        self.rect.y = (int(self.initial_y / 10)) * 10

        # I do this so that I can change calculated_x and calculated_y without accidentally
        # changing the actual rect x and y.
        self.calculated_x = self.rect.y - 0
        self.calculated_y = self.rect.y - 0


    # FIXME: This equation does not work as intended. It rounds it to spots of 10 instead
    # of 20 like desired.
    def set_display_x(self):
        self.rect.x = (int(self.calculated_x / 10)) * 10

    def set_display_y(self):
        self.rect.y = (int(self.calculated_y / 10)) * 10

    def move(self, x_movement, y_movement):
        self.calculated_x += x_movement
        self.calculated_y += y_movement

        self.set_display_x()
        self.set_display_y()

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
        self.rect.x = (int(self.initial_x / 10)) * 10

        self.initial_y = random.randrange(1, (display_height - self.side_length))
        # This gives us the column the apple will be in instead of the raw coordinates.
        self.rect.y = (int(self.initial_x / 10)) * 10
