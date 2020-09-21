import pygame
from pygame.sprite import Sprite

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
	
	def update(self):
		self.x += (self.settings.alien_speed_factor * 
			self.settings.fleet_direction)
		self.rect.x = self.x
		# self.rect.y += self.settings.alien_speed_factor/2
	
	def check_edge(self):
		screen_rect = self.screen.get_rect()
		if self.rect.left <= 0 or self.rect.right >= screen_rect.right:
			return True
			
	def blitme(self):
		self.screen.blit(self.image,self.rect)