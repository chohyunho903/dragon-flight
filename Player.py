import pygame
from pygame.time import delay

import gameWolrd
from Bullet import Bullet


class Player:
    playerImage = [pygame.image.load(".//image//player//Frame"+str(i)+".png") for i in range(16)]
    for i in range(16):
        playerImage[i] = pygame.transform.scale(playerImage[i], (300, 220))
        playerImage[i] = pygame.transform.flip(playerImage[i], False, True)
        playerImage[i].set_colorkey((254, 254, 254))

    def __init__(self, x,y):
        self.x, self.y = x, y
        self.frame = 0
        self.bulletDelay = 0
        self.bulletSpeed = 20
        self.skill = 0
        self.startSkillTime = 0
        self.hp = 3

        pygame.mixer.music.load(".//BGM.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)


    def update(self, pos):
        self.x = pos[0] - 150
        self.frame = (self.frame + 1) % 16
        self.bulletDelay = (self.bulletDelay + 1) % self.bulletSpeed
        self.addBullet()
        self.updateSkillTime()


    def draw(self):
        gameWolrd.screen.blit(Player.playerImage[self.frame], (self.x, self.y))
        # self.drawHitBox()

    def getHitBox(self):
        return self.x + 100, self.y + 100, self.x + 200, self.y + 150

    def drawHitBox(self):
        x1, y1, x2, y2 = self.getHitBox()
        points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        pygame.draw.polygon(gameWolrd.screen, (0, 0, 0), points, 1)

    def addBullet(self):
        if self.bulletDelay == 0:
            gameWolrd.add_object(Bullet(self.x, self.skill),3)

    def collision(self, type, other):
        if type == "PlayerToMonster":
            self.hp -= 1
            if self.hp <= 0:
                font = pygame.font.SysFont(None, 140)  # 시스템 폰트, 크기 36
                text = font.render("GAME OVER", True, (255, 255, 255))
                gameWolrd.screen.blit(text, (0, 200))  # (100, 100) 위치에 출력

                font = pygame.font.SysFont(None, 35)  # 시스템 폰트, 크기 36
                text = font.render("The program will shut down in 3 seconds", True, (255, 255, 255))
                gameWolrd.screen.blit(text, (50, 400))  # (100, 100) 위치에 출력

                gameWolrd.running = False

    def useSkill(self):
        if self.skill == 0:
            self.startSkillTime = pygame.time.get_ticks()
            self.skill = 1
            self.bulletSpeed = 10

    def updateSkillTime(self):
        if self.skill == 1:
            if (pygame.time.get_ticks() - self.startSkillTime) >= 10000:  # 1만틱 = 10초
                self.skill = 0
                self.bulletSpeed = 20
    def getPlayerHp(self):
        return self.hp