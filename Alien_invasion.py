import sys

from settings import Settings
from ship import Ship
from bullet import Bullet

import pygame

class AlienInvasion:
	"""Class for control resource game"""

	def __init__(self):
		"""Initializing the game and creating game resources"""

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption('Alien Invasion')
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		

	def run_game(self):
		"""Run main game cycle"""

		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()

			
	def _check_events(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Reacts on keydown"""

		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Reacts on keyup"""

		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False


	def _fire_bullet(self):
		"""Created new bullet and addhis in group bullets"""

		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update position bullets and deleted old"""

		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)


	def _update_screen(self):

		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		pygame.display.flip()

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()