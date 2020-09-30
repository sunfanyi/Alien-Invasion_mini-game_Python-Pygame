from settings import Settings
from game_stats import GameStats

ai_settings = Settings()
stats = GameStats(ai_settings)
with open('highest_score.txt','w') as file_object:
	file_object.w = 0
