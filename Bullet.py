import pygame

import gameWolrd


class Bullet:
    defaultBulletImage = pygame.image.load(".//image//Bullets//Bullet.png")
    skillBulletImage = pygame.image.load(".//image//Bullets//Bullet2.png")

    speed = 10

    damage = [50, 150]
    def __init__(self, x, type=0):
        self.x, self.y = x, 730
        self.type = type # 0: 평타딜, 1: 스킬딜 // Bullet.damage[self.type]로 damage 결정.
        self.sound = pygame.mixer.Sound(".//Bullet.wav")
        self.sound.set_volume(0.2)
        self.sound.play()

    def update(self, pos):
        self.y -= Bullet.speed
        if self.y <= -50:
            gameWolrd.remove_object(self)

    def draw(self):
        if self.type == 0:
            gameWolrd.screen.blit(Bullet.defaultBulletImage, (self.x + 140, self.y))
        else:
            gameWolrd.screen.blit(Bullet.skillBulletImage, (self.x + 95, self.y))
        # self.drawHitBox()

    def getHitBox(self):
        if self.type == 0:
            return self.x + 140, self.y, self.x + 160, self.y + 40
        else:
            return self.x + 95, self.y, self.x + 205, self.y + 100

    def drawHitBox(self):
        x1, y1, x2, y2 = self.getHitBox()
        points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        pygame.draw.polygon(gameWolrd.screen, (0, 0, 0), points, 1)

    def collision(self, type, other):
        if type == "bulletToMonster":
            gameWolrd.remove_object(self)

    def getDamage(self):
        return Bullet.damage[self.type]


