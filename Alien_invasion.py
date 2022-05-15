import sys

from settings import Settings

import pygame

class AlienInvasion:
	"""Class for control resource game"""

	def __init__(self):
		"""Initializing the game and creating game resources"""

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption('Alien Invasion')
		

	def run_game(self):
		"""Run main game cycle"""

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.screen.fill(self.settings.bg_color)

			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()