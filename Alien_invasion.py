import sys
from time import sleep

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

import pygame

class AlienInvasion:
	"""Class for control resource game"""


	def __init__(self):
		"""Initializing the game and creating game resources"""

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption('Alien Invasion')

		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		self.play_button = Button(self, 'Play')
		

	def run_game(self):
		"""Run main game cycle"""

		while True:
			self._check_events()
			
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
			
			self._update_screen()

			
	def _check_events(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
			

	def _check_play_button(self, mouse_pos):
		"""Run new game when play button has been down"""

		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self.settings.intialize_dynamic_settings()
			self.start_game()
			

	def start_game(self):
		
		self.stats.reset_stats()
		self.stats.game_active = True
		self.sb.prep_score()

		self.aliens.empty()
		self.bullets.empty()

		self._create_fleet()
		self.ship.center_ship()

		pygame.mouse.set_visible(False)


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

		self._check_bullet_alien_collision()


	def _check_bullet_alien_collision(self):
		"""Respond to bullet-alien collision"""

		collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

		if collision:
			self.stats.score += self.settings.alien_point
			self.sb.prep_score()


	def _update_aliens(self):
		"""Update position alien in fleet"""

		self._check_fleet_ebges()
		self.aliens.update()

		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		self._check_aliens_bottom()


	def _check_aliens_bottom(self):
		"""Checks if aliens have reached the bottom of the screen"""

		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break


	def _ship_hit(self):
		"""Handles coliision ship with alien"""

		if self.stats.ship_left > 0:
			self.stats.ship_left -= 1
	
			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()

			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _create_fleet(self):
		"""Created fleet invasion"""

		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_alien_x = available_space_x // (2 * alien_width)

		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		for row_number in range(number_rows):
			for alien_number in range(number_alien_x):
				self._create_alien(alien_number, row_number)
	

	def _create_alien(self, alien_number, row_number):
		"""Created alien and move him in row"""

		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)


	def _check_fleet_ebges(self):
		"""React when reaching the edge of the screen"""

		for alien in self.aliens.sprites():
			if alien._check_edges():
				self._change_fleet_direction()
				break


	def _change_fleet_direction(self):
		"""Lover the gleet and changes direction"""

		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed

		self.settings.fleet_direction *= -1


	def _update_screen(self):

		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		self.sb.show_score()

		if not self.stats.game_active:
			self.play_button.draw_button()

		pygame.display.flip()


if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()