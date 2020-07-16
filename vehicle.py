import pygame

class spaceship:
    def __init__(self, mainGame):
        self.screen = mainGame.screen
        self.screen_rect = mainGame.screen.get_rect()

        self.impage = pygame.image.load()