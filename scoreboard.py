import pygame.font
from pygame.sprite import Group

from ship import Ship

class ScoreBoard():
	def __init__(self,settings,stats,screen):
		self.screen = screen
		self.settings = settings
		self.stats = stats
		self.screen_rect = self.screen.get_rect()
		
		self.text_color = 30,30,30
		self.font = pygame.font.SysFont(None,48)
		
		self.prep_score()
		self.prep_highest_score()
		self.prep_level()
		self.prep_ships()
		
	def prep_score(self):
		#round 表示保留小数，-1即保留到10整位
		rounded_score = round(self.stats.score,-1)
		score_str = '{:,}'.format(rounded_score)
		self.score_image = self.font.render(score_str,True,
			self.text_color,self.settings.bg_color)
		
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right-20
		self.score_rect.top = 20
		
	def prep_highest_score(self):
		highest_score = round(self.stats.highest_score,-1)
		highest_score_str = '{:,}'.format(highest_score)
		# highest_display = 'Highest: ' + highest_score_str
		self.highest_score_image = self.font.render(highest_score_str,
			True,self.text_color,self.settings.bg_color)
			
		self.highest_score_rect = self.highest_score_image.get_rect()
		self.highest_score_rect.centerx = self.screen_rect.centerx
		self.highest_score_rect.top = self.score_rect.top
	
	def prep_level(self):
		self.level_image = self.font.render(str(self.stats.level),True,
			self.text_color,self.settings.bg_color)
			
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
	def prep_ships(self):
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.settings,self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.highest_score_image,
			self.highest_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		#在左上角画剩余的ship
		self.ships.draw(self.screen)
