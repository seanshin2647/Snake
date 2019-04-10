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
        self.body_chain_list = pygame.sprite.Group()

        # Strictly speaking, I don't need this list to exist. However, I am using
        # it to check if an apple exists on the board at the moment. I might
        # later change this to a boolean variable that is set to False when the player
        # eats an apple.
        self.apple_list = pygame.sprite.Group()

        self.head = Player_Head(display_width, display_height)
        self.all_sprites_list.add(self.head)
        self.body_chain_list.add(self.head)

        # Useful for creating new body parts.
        # This creates a new list of the body chain.
        self.create_body_list()

        # I'm sorry for this. Forgive me, whoever is reading this. I should have found
        # a better way to do it than this.
        self.body = Body(self.listed_body_chain[0].rect.x, self.listed_body_chain[0].rect.y,
            display_width, display_height)
        self.all_sprites_list.add(self.body)
        self.body_chain_list.add(self.body)

        self.apple = Apple(display_width, display_height)
        self.all_sprites_list.add(self.apple)
        self.apple_list.add(self.apple)

        # Player and game specific variables.
        self.x_movement = 5
        self.y_movement = 0

        self.score = 0

    def create_body_list(self):
        self.listed_body_chain = list(self.body_chain_list)

    def render(self, display):
        self.all_sprites_list.draw(display)

    def create_apple(self):
        apple = Apple()
        self.all_sprites_list.add(self.apple)
        self.apple_list.add(self.apple)

    def create_body(self, chain_length, display_width, display_height):
        self.body = Body(self.listed_body_chain[chain_length].rect.x, self.listed_body_chain[chain_length].rect.y,
            display_width, display_height)
        self.all_sprites_list.add(self.body)
        self.body_chain_list.add(self.body)

        # I need this here to update the list.
        self.create_body_list()

    def eat_apple(self, display_width, display_height):
        if pygame.sprite.spritecollide(self.head, self.apple_list, True):
            # FIXME: Does not work. List is continually out of range.
            self.create_body((len(self.body_chain_list) - 1), display_width, display_height)
            self.score += 1

    # TODO: Actually make this work. I have it so that it will probably have the entire
    # body move at once with the head. I just left it like that for now to get the 
    # basic game off the ground.

    # TODO: Have the body parts move into the place the previous part occupied.
    # That way, it looks like its moving without having to
    # code a bunch of weird things that you might have had to do.
    # Maybe use a for loop to append the x and y positions to a list
    # so that you can track the current calculated position and use the index that the
    # variable that is tracking points to to move the entire snake body naturally.
    
    def update(self, display_width, display_height):
        # TODO: Make a for loop for this.
        self.head.move(self.x_movement, self.y_movement)

        self.eat_apple(display_width, display_height)

        if len(self.apple_list) == 0:
            self.create_apple()

        self.all_sprites_list.update()

    def collide_self(self):
        if pygame.sprite.spritecollide(self.head, self.body_chain_list, False):
            return True

    def collide_wall(self, display_width, display_height):
        if self.head.rect.x >= (display_width - self.head.side_length):
            return True
        elif self.head.rect.x <= 0:
            return True

        if self.head.rect.y >= (display_height - self.head.side_length):
            return True
        elif self.head.rect.y <= 0:
            return True

    def handle_events(self, pressed_buttons, display_width, display_height):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()

            # TODO: Find a way to shorten this. Maybe use Kevin's stack overflow answer.
            # Super ugly. 

            # TODO: Change this part to work similiar to a key down and up as right now,
            # it only triggers once you have let go of the key instead of pushed
            # down, which is a problem.
            if pressed_buttons[pygame.K_w]:
                self.y_movement = -5
                self.x_movement = 0

            if pressed_buttons[pygame.K_s]:
                self.y_movement = 5
                self.x_movement = 0

            if pressed_buttons[pygame.K_a]:
                self.x_movement = -5
                self.y_movement = 0

            if pressed_buttons[pygame.K_d]:
                self.x_movement = 5
                self.y_movement = 0

        # TODO: Make this transition to the end screen.
        if self.collide_wall(display_width, display_height):
            print(self.score)
            kill_game()

        #or self.collide_self()
            
