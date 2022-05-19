import sys

from settings import Settings
from ship import Ship

import pygame

class AlienInvasion:
	"""Class for control resource game"""

	def __init__(self):
		"""Initializing the game and creating game resources"""

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Alien Invasion')
		self.ship = Ship(self)
		

	def run_game(self):
		"""Run main game cycle"""

		while True:
			self._check_events()

			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			pygame.display.flip()

	def _check_events(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()