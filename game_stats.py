class GameStats():
	def __init__(self,settings):
		self.settings = settings
		self.reset_stats()
		self.game_active = False
		self.break_record = False
		with open('highest_score.txt') as file_object:
			#file_object.read()只能调用一次，第二次后返回的为空
			content = file_object.read()
			if content:
				self.highest_score = int(content)
			else:
				self.highest_score = 0
				
	def reset_stats(self):
		self.ship_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
