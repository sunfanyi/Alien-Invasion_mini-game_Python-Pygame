import pygame
from pygame.sprite import Sprite
import random as rn

class Alien(Sprite):
	def __init__(self,settings,screen):
		super().__init__()
		self.screen = screen
		self.settings = settings
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		if rn.random() > 0.5:
			self.alien_direction = 1
		else:
			self.alien_direction = -1
			
		self.alien_speed_factor_x = \
			rn.uniform(settings.alien_min_speed_x,
				settings.alien_max_speed_x)
		self.alien_speed_factor_y = \
			rn.uniform(settings.alien_min_speed_y,
				settings.alien_max_speed_y)
	
	def update(self):
		self.x += (self.alien_speed_factor_x * 
			self.alien_direction)
		self.rect.x = self.x
		self.y += self.alien_speed_factor_y
		self.rect.y = self.y
	
	def check_edge(self):
		screen_rect = self.screen.get_rect()
		if self.rect.left <= 0 or self.rect.right >= screen_rect.right:
			return True
			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
