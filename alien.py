import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, mainGame):
        super().__init__()
        self.screen = mainGame.mainScreen
        self.setting = mainGame.setting

        self.image = pygame.image.load('image/alien.png')
        self.image = pygame.transform.scale(self.image, (80,30))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True