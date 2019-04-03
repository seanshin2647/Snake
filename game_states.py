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

        self.head = Player_Head()
        self.all_sprites_list.add(self.head)
        self.body_chain_list.add(self.head)

        self.body = Body(body_chain_list[0].rect.x, body_chain_list[0].rect.y)
        self.all_sprites_list.add(self.body)
        self.body_chain_list.add(self.body)

        self.apple = Apple()
        self.all_sprites_list.add(self.apple)

        # Player and game specific variables.
        self.x_movement = 8
        self.y_movement = 8

        self.score = 0

    def render(self, display):
        self.all_sprites_list.draw(display)
