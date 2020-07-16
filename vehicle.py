import pygame

class Spaceship:
    def __init__(self, mainGame):
        self.screen = mainGame.mainScreen
        self.screen_rect = mainGame.mainScreen.get_rect()
        self.setting = mainGame.setting

        self.image = pygame.image.load('image/starship.png')
        self.image = pygame.transform.scale(self.image, (51, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.movingRight = False
        self.movingLeft = False
        self.movingUp = False
        self.movingDown = False

    def update(self):
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.x += self.setting.shipSpeed
        if self.movingUp and self.rect.top > 0:
            self.y -= self.setting.shipSpeed
        if self.movingDown and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.shipSpeed
        if self.movingLeft and self.rect.left > 0:
            self.x -= self.setting.shipSpeed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)