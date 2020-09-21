import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien invasion')
	
	my_ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	stats = GameStats(ai_settings)
	play_button = Button(screen,'Play')
	sb = ScoreBoard(ai_settings,stats,screen)
	gf.create_fleet(ai_settings,screen,my_ship,aliens)
	
	while True:
		gf.check_event(ai_settings,stats,sb,screen,my_ship,bullets,
			aliens,play_button)
		
		if stats.game_active:
			my_ship.update()
			gf.update_bullets(ai_settings,stats,sb,screen,my_ship,
				bullets,aliens)
			gf.update_aliens(ai_settings,stats,sb,screen,my_ship,bullets,
				aliens)
			
		gf.update_screen(ai_settings,stats,sb,screen,my_ship,bullets,
			aliens,play_button)
		
run_game()
