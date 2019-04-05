from game_states import *

pygame.init()

FPS = 60
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
DISPLAY - pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])

clock = pygame.time.Clock()

def main_loop():
    game_state = Game_State()
    # TODO: Change this to something else.
    while True:

        pressed_buttons = pygame.key.get_pressed()
        game_state.handle_events(pressed_buttons, DISPLAY_WIDTH, DISPLAY_HEIGHT)

        game_state.update()
        DISPLAY.fill(LIGHT_GREEN)

        game_state.render(DISPLAY)

        pygame.display.update()
        clock.tick(FPS)

main_loop()
