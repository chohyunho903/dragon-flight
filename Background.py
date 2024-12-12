import pygame

from gameWolrd import screen, screen_width, screen_height


class Background:
    moveSpeed = 5
    backgroundImage = pygame.image.load(".//image//background//background.png")
    backgroundImage = pygame.transform.scale(backgroundImage, (screen_width, screen_height))

    def __init__(self,x, y):
        self.x, self.y = x, y

    def update(self, pos):
        self.y += Background.moveSpeed
        if self.y >= screen_height:
            self.y = -(screen_height * 2)

    def draw(self):
        screen.blit(Background.backgroundImage, (self.x, self.y))
