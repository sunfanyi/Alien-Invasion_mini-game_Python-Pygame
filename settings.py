class Settings():
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = 230,230,230
		self.ship_limit = 2

		self.bullet_width = 12
		self.bullet_height = 50
		self.bullet_color = 60,60,60
		self.bullets_allowed = 5
	
		
		self.speed_up_factor = 1.07
		self.score_scale = 1.4
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 2
		self.bullet_speed_factor = 3
		self.alien_max_speed_x = 1.4
		self.alien_min_speed_x = 0.6
		self.alien_speed_factor_y = 0.05
		self.alien_points = 50
		
	def increase_speed(self):
		self.ship_speed_factor *= self.speed_up_factor
		self.bullet_speed_factor *= self.speed_up_factor
		self.alien_max_speed_x *= self.speed_up_factor
		self.alien_min_speed_x *= self.speed_up_factor
		self.alien_speed_factor_y *= (self.speed_up_factor - 
			(self.speed_up_factor-1)/2)
		self.alien_points = int(self.alien_points * self.score_scale)
	
