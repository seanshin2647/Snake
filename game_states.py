from game_classes import *

def kill_game():
    pygame.quit()
    quit()

class State():
    def __init__(self):
        pass

    def render(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self):
        raise NotImplementedError

class Game_State(State):
    def __init__(self, display_width, display_height):
        super().__init__()

        # The object related initialzing.
        self.all_sprites_list = pygame.sprite.Group()
        self.segment_list = pygame.sprite.Group()

        self.x_locations = []
        self.y_locations = []

        # I am using it to check if an apple exists on the board at the moment. I might
        # later change this to a boolean variable that is set to False when the player
        # eats an apple.
        self.apple_list = pygame.sprite.Group()

        self.head = Player_Head(display_width, display_height)
        self.all_sprites_list.add(self.head)

        self.initialize_segments(display_width, display_height)
        self.initialize_x_y_lists()

        self.apple = Apple(display_width, display_height)
        self.all_sprites_list.add(self.apple)
        self.apple_list.add(self.apple)

        self.update_segment_list()

        # Player and game specific variables.
        self.general_movement = 5
        self.x_movement = self.general_movement
        self.y_movement = 0

        self.head.rect.x += self.head.side_length

        self.score = 0

    # TODO: Have this so that the segments start behind the player's head, not on top of it.
    def initialize_segments(self, display_width, display_height):
        self.body = Body(1)
        self.all_sprites_list.add(self.body)
        self.segment_list.add(self.body)

        self.update_segment_list()

        self.create_body((len(self.listed_segments) + 1))

        self.update_segment_list()

    def initialize_x_y_lists(self):
        for x in range((len(self.segment_list) * 5)):
            self.x_locations.append(self.head.rect.x)
        
        for y in range((len(self.segment_list) * 5)):
            self.y_locations.append(self.head.rect.y)

    def update_segment_list(self):
        self.listed_segments = list(self.segment_list)

###
    def render(self, display):
        self.all_sprites_list.draw(display)
###

    def create_body(self, chain_length):
        self.body = Body((len(self.listed_segments) + 1))
        self.all_sprites_list.add(self.body)
        self.segment_list.add(self.body)
        self.update_segment_list()

    def eat_apple(self, display_width, display_height):
        if pygame.sprite.spritecollide(self.head, self.apple_list, True):
            # FIXME: Does not work. List is continually out of range.
            self.create_body((len(self.segment_list)))
            self.score += 1

    def create_apple(self, display_width, display_height):
        self.apple = Apple(display_width, display_height)
        self.all_sprites_list.add(self.apple)
        self.apple_list.add(self.apple)

    def snake_movement(self):
        print("x_locations length: ", len(self.x_locations))
        print("y_locations length: ", len(self.y_locations))
        for amount in range (len(self.listed_segments) - 1):
            self.listed_segments[amount].location += 1
            print(self.listed_segments[amount].location)
            self.listed_segments[amount].rect.x, self.listed_segments[amount].rect.y = (
                self.x_locations[self.listed_segments[amount].location], 
                self.y_locations[self.listed_segments[amount].location])

    def x_movement_append(self):
        self.x_locations.append(self.head.rect.x)

    def y_movement_append(self):
        self.y_location.append(self.head.y)

    def head_movement(self):
        if self.x_movement != 0:
            if self.x_movement > 0:
                self.head.rect.x += self.x_movement
                self.x_movement_append()

            elif self.x_movement < 0:
                self.head.rect.x += self.x_movement
                self.x_movement_append()

        if self.y_movement != 0:
            if self.y_movement > 0:
                self.head.rect.y += self.y_movement
                self.y_movement_append()

            elif self.y_movement < 0:
                self.head.rect.y += self.y_movement
                self.y_movement_append()
    
###
    def update(self, display_width, display_height):
        self.snake_movement()
        self.head_movement()

        self.eat_apple(display_width, display_height)

        if len(self.apple_list) == 0:
            self.create_apple(display_width, display_height)

        self.all_sprites_list.update()
###

    def collide_self(self):
        if pygame.sprite.spritecollide(self.head, self.segment_list, False):
            return True

    def collide_wall(self, display_width, display_height):
        if self.x_movement != 0:
            if self.x_movement > 0:
                if (self.head.rect.x + self.head.side_length) >= display_width:
                    return True
            elif self.x_movement < 0:
                if self.head.rect.x <= 0:
                    return True

        if self.y_movement != 0:
            if self.y_movement > 0:
                if (self.head.rect.y + self.head.side_length) >= display_height:
                    return True
            elif self.y_movement < 0:
                if self.head.rect.y <= 0:
                    return True

###
    def handle_events(self, pressed_buttons, display_width, display_height):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()

            # TODO: Clean this part up. Please

            # TODO: Change this part to work similiar to a key down and up as right now,
            # it only triggers once you have let go of the key instead of pushed
            # down, which is a problem.

            if self.x_movement < 0:
                if pressed_buttons[pygame.K_w]:
                    self.head.gridset_x(0)
                    self.y_movement = -1 * self.general_movement
                    self.x_movement = 0

                if pressed_buttons[pygame.K_s]:
                    self.head.gridset_x(0)
                    self.y_movement = self.general_movement
                    self.x_movement = 0

            elif self.x_movement > 0:
                if pressed_buttons[pygame.K_w]:
                    self.head.gridset_x(self.head.side_length)
                    self.y_movement = -1 * self.general_movement
                    self.x_movement = 0

                if pressed_buttons[pygame.K_s]:
                    self.head.gridset_x(self.head.side_length)
                    self.y_movement = self.general_movement
                    self.x_movement = 0

            if self.y_movement < 0:
                if pressed_buttons[pygame.K_d]:
                    self.head.gridset_y(0)
                    self.y_movement = 0
                    self.x_movement = self.general_movement

                if pressed_buttons[pygame.K_a]:
                    self.head.gridset_y(0)
                    self.y_movement = 0
                    self.x_movement = -1 * self.general_movement

            elif self.y_movement > 0:
                if pressed_buttons[pygame.K_d]:
                    self.head.gridset_y(self.head.side_length)
                    self.y_movement = 0
                    self.x_movement = self.general_movement

                if pressed_buttons[pygame.K_a]:
                    self.head.gridset_y(self.head.side_length)
                    self.y_movement = 0
                    self.x_movement = -1 * self.general_movement

        # TODO: Make this transition to the end screen.
        if self.collide_wall(display_width, display_height):
            print("Score: ", self.score)
            kill_game()

        #or self.collide_self()
###
