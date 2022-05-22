import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Class for createrd one alien"""
	
	def __init__(self, ai_game):
		"""Initializing alien and create his start position """

		super().__init__()
		self.screen = ai_game.screen

		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)