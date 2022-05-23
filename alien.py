import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Class for createrd one alien"""
	
	def __init__(self, ai_game):
		"""Initializing alien and create his start position """

		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def _check_edges(self):
		"""Return True if alien located at the edge of the screen"""

		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""Moved alien on the right or left"""

		self.x += self.settings.alien_speed * self.settings.fleet_direction
		self.rect.x = self.x