# Achieved initial capabilities on 0603 Hours UTC - 30/4/2019
# Brought tears of joy to my eyes. "It works" I exclaimed with joy.

from game_states import *

pygame.init()

FPS = 60
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600
DISPLAY = pygame.display.set_mode([DISPLAY_WIDTH, DISPLAY_HEIGHT])
5
clock = pygame.time.Clock()

def main_loop():
    game_state = Game_State(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    # TODO: Change this to something else.
    while True:

        pressed_buttons = pygame.key.get_pressed()
        game_state.handle_events(pressed_buttons, DISPLAY_WIDTH, DISPLAY_HEIGHT)

        game_state.update(DISPLAY_WIDTH, DISPLAY_HEIGHT)
        DISPLAY.fill(LIGHT_GREEN)

        game_state.render(DISPLAY)

        pygame.display.update()
        clock.tick(FPS)

main_loop()
