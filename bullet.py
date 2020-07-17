import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, mainGame):
        super().__init__()
        self.screen = mainGame.mainScreen
        self.setting = mainGame.setting
        self.color = self.setting.bullet_color

        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = mainGame.spaceShip.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)