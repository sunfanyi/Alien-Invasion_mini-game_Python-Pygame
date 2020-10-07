import pygame

class ShipExplosion():
	def __init__(self,screen,ship):
		self.screen = screen
		self.ship = ship
		
		self.image = pygame.image.load('images/ship_explosion.bmp')
		self.rect = self.image.get_rect()
		
	def get_position(self):
		#必须只能在撞击发生时获取位置信息，否则位置信息将变为主程序中调用
		# ShipElosion时飞船的起始位置
		self.rect.center = self.ship.rect.center
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)

