import sys
import pygame
from setting import setting
from vehicle import Spaceship

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
	def runGame(self):
		while True:
			self._checkEvent()
			self.spaceShip.update()
			self._updateScreen()
			pygame.display.flip()

# Main Game
myGame = MainGame()
myGame.runGame()