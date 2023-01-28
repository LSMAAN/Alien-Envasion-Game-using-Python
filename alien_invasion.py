import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    FPS = 150
    clock = pygame.time.Clock()

    #Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Make an alien.
    alien = Alien(ai_settings, screen)

    #Make a group to store bullets in, and a group of aliens.
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    while True:
        clock.tick(FPS)
        
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets
                         , play_button)

run_game()
