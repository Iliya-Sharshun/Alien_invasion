import pygame

class Ship():
	"""Class for control ship"""

	def __init__(self, ai_game):
		"""Initializing ship and created his start position"""

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Uodate position ship"""

		if self.moving_right:
			self.rect.x += 1
		if self.moving_left:
			self.rect.x -= 1

	def blitme(self):
		"""Created ship in current position"""

		self.screen.blit(self.image, self.rect)