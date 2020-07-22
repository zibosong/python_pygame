import sys
import pygame
from setting import setting
from vehicle import Spaceship
from bullet import Bullet
from alien import Alien

class MainGame:
	def __init__(self):
		""" initialization """
		pygame.init()
		""" draw main screen """
		self.setting = setting()
		self.mainScreen = pygame.display.set_mode(size=(self.setting.screenWidth, self.setting.screenHeight))
		pygame.display.set_caption(self.setting.caption)
		""" load vehicle """
		self.spaceShip = Spaceship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self._create_fleet()

	""" 		Aliens and Fleet 				"""
	def _create_alien(self, alien_number, row_number):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _create_fleet(self):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.setting.screenWidth - (1 * alien_width)
		number_alien_x = available_space_x // (2 * alien_width)

		ship_height = self.spaceShip.rect.height
		available_space_y = (self.setting.screenHeight - (6 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		for row_number in range (number_rows):
			for alien_number in range (number_alien_x):
				self._create_alien(alien_number, row_number)

	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.setting.fleet_drop_speed
		self.setting.fleet_direction *= -1

	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()


	"""			Bullets 			"""
	def _fire_bullet(self):
		new_bullet = Bullet(self)
		if len(self.bullets) < self.setting.bullets_allowed:
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		self.bullets.update()
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

	""" Check keyboard inpurt"""
	def _checkEvent(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.spaceShip.movingRight = True
				elif event.key == pygame.K_UP:
					self.spaceShip.movingUp = True
				elif event.key == pygame.K_DOWN:
					self.spaceShip.movingDown = True
				elif event.key == pygame.K_LEFT:
					self.spaceShip.movingLeft = True
				elif event.key == pygame.K_q:
					sys.exit()
				elif event.key == pygame.K_SPACE:
					self._fire_bullet()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.spaceShip.movingRight = False
				elif event.key == pygame.K_UP:
					self.spaceShip.movingUp = False
				elif event.key == pygame.K_DOWN:
					self.spaceShip.movingDown = False
				elif event.key == pygame.K_LEFT:
					self.spaceShip.movingLeft = False

	def _updateScreen(self):
		self.mainScreen.fill(self.setting.bgColor)
		self.spaceShip.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		#self.aliens.draw(self.mainScreen)

	def runGame(self):
		while True:
			self._checkEvent()
			self.spaceShip.update()
			self._update_bullets()
			#self._update_aliens()
			self._updateScreen()
			pygame.display.flip()

# Main Game
myGame = MainGame()
myGame.runGame()