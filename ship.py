import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,settings,screen):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.x = float(self.rect.centerx)
		self.y = float(self.rect.centery)
		
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
			
	def update(self):
		self.ship_moving()
		self.rect.centerx = self.x
		self.rect.centery = self.y
		
	def ship_moving(self):
		if self.moving_right and (self.rect.right <= 
				self.screen_rect.right):
			self.x += self.settings.ship_speed_factor
		if self.moving_left and self.rect.left >= 0:
			self.x -= self.settings.ship_speed_factor
		if self.moving_up and self.rect.top >= 0:
			self.y -= self.settings.ship_speed_factor*2/3
		if self.moving_down and (self.rect.bottom <= 
				self.screen_rect.bottom):
			self.y += self.settings.ship_speed_factor*2/3
		
	def relocate_ship(self):
		self.x = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#下一步十分重要，否则update()的时候rect.centery会变成之前ship_moving()
		#	里改变了的self.y，即重生点y坐标会回到死亡点的y坐标，而不是到最底下
		self.y = self.rect.y
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
