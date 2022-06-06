class Settings():
	"""Class for storing game settings"""

	def __init__(self):
		"""Initializing game settings"""

		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		
		self.ship_limit = 3

		self.bullet_width = 30
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 3

		self.fleet_drop_speed = 10
		self.fleet_direction = 1


		self.speedup_scale = 1.1
		self.intialize_dynamic_settings()

	def intialize_dynamic_settings(self):
		"""Initializing  settings who will be change in game time"""

		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0
		self.fleet_direction = 1
		self.alien_point = 50

	def increase_speed(self):
		"""Increasing speed settings"""

		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale