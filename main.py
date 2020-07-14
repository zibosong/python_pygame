import sys
import pygame
from setting import setting

class mainGame:
	def __init__(self):
		pygame.init()
		self.setting = setting()
		mainScreen = pygame.display.set_mode(size=(self.setting.screenWidth, self.setting.screenHeight))

	def runGame(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			pygame.display.flip()

# Main Game
myGame = mainGame()
myGame.runGame()