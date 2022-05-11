import sys

import pygame

class AlienInvasion:
	"""Class for control resource game"""

	def __init__(self):
		"""Initializing the game and creating game resources"""

		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption('Alien Invasion')

	def run_game(self):
		"""Run main game cycle"""

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()