class GameStats():
	"""Class for statistics tracking"""

	def __init__(self, ai_game):
		"""Itializing statistic"""

		self.settings = ai_game.settings
		self.reset_stats()

		self.game_active = False


	def reset_stats(self):
		"""Itializes statistics that change guring the game"""

		self.ship_left = self.settings.ship_limit