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

        self.all_sprites_list = pygame.sprite.Group()
        self.body_chain_list = pygame.sprite.Group()

        self.head = Player_Head()
        self.all_sprites_list.add(self.head)
        self.body_chain_list.add(self.head)

        self.body = Body(body_chain_list[0].rect.x, body_chain_list[0].rect.y)
        self.all_sprites_list.add(self.body)
        self.body_chain_list.add(self.body)
