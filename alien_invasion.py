import pygame


from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_colour = (230, 230, 230)
    ship = Ship(screen)


    while True:
        gf.check_events()

        screen.fill(ai_settings.bg_colour)
        ship.blitme()

        pygame.display.flip()

run_game()

