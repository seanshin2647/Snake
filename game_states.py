from game_classes import *

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
    def __init__(self):
        super().__init__()

        # The object related initialzing.
        self.all_sprites_list = pygame.sprite.Group()
        self.body_chain_list = pygame.sprite.Group()

        # Strictly speaking, I don't need this list to exist. However, I am using
        # it to check if an apple exists on the board at the moment. I might
        # later change this to a boolean variable that is set to False when the player
        # eats an apple.
        self.apple_list = pygame.sprite.Group()

        self.head = Player_Head()
        self.all_sprites_list.add(self.head)
        self.body_chain_list.add(self.head)

        self.body = Body(body_chain_list[0].rect.x, body_chain_list[0].rect.y)
        self.all_sprites_list.add(self.body)
        self.body_chain_list.add(self.body)

        self.apple = Apple()
        self.all_sprites_list.add(self.apple)
        self.apple_list.add(self.apple)

        # Player and game specific variables.
        self.x_movement = 8
        self.y_movement = 8

        self.elapsed_movement = 0

        self.score = 0

    def render(self, display):
        self.all_sprites_list.draw(display)

    def create_apple(self):
        apple = Apple()
        self.all_sprites_list.add(self.apple)
        self.apple_list.add(self.apple)

    def create_body(self, chain_length):
        self.body = Body(body_chain_list[chain_length + 1].rect.x, body_chain_list[chain_length + 1].rect.y)
        self.all_sprites_list.add(self.body)
        self.body_chain_list.add(self.body)

    def eat_apple(self):
        if pygame.sprite.spritecollide(self.head, self.apple_list, True):
            create_body(len(body_chain_list))
            self.score += 1


    # TODO: Actually make this work. I have it so that it will probably have the entire
    # body move at once with the head. I just left it like that for now to get the 
    # basic game off the ground.
    def update(self):
        self.player.rect.x += self.x_movement
        self.player.rect.y += self.y_movement

        eat_apple()

        # TODO: Have the apple spawn in a location not taken up by the player's body.
        if len(apple_list) == 0:
            create_apple()

        self.all_sprites_list.update()