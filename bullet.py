import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Class for controll bullets that have been fired by a ship"""

		def __init__(self, ai_game):
			"""Created bullet object"""

			super.__init__()
			self,screen = ai_game.screen
			self.settings = ai_game.settings
			self.color = self.settings.bullet_color

			self.rect = pygame.Rect(0, 0, self.settings.screen_width, self.settings.screen_height)
			self.rect.midtop = ai_game.ship.rect.midtop

			self.y = float(self.rect.y)

		def update(self):
			"""Moved bullet up the screen"""

			self.y -= self.settings.bullet_speed
			self.rect.y = self.y

		def draw_bullet(self):
			"""Draw bullet on the screen"""

			pygame.draw.rect(self.screen, self.color, self.rect)