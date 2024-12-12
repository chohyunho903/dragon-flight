import random

import pygame

import gameWolrd


class Monster:
    moveSpeed = 5
    MonsterImage = [pygame.image.load(".//image//Monster//Monster" + str(i) + ".png") for i in range(20)]
    for i in range(20):
        MonsterImage[i] = pygame.transform.scale(MonsterImage[i], (400, 250))

        MonsterImage[i].set_colorkey((254, 254, 254))

    def __init__(self, x, y, hp):
        self.x, self.y = x - 150, y
        self.maxHp = hp
        self.hp = hp
        self.frame = 0

    def update(self, pos):
        self.y += Monster.moveSpeed
        self.frame = (self.frame + 1) % 20

    def draw(self):
        gameWolrd.screen.blit(Monster.MonsterImage[self.frame], (self.x, self.y))
        pygame.draw.rect(gameWolrd.screen, (0, 0, 0), (self.x + 165, self.y + 50, 60, 10))
        pygame.draw.rect(gameWolrd.screen, (255, 0, 0), (self.x + 165, self.y + 50,
                                                         60 / (self.maxHp / self.hp), 10))
        # self.drawHitBox()

    def removeCheck(self):
        if self.y >= gameWolrd.screen_height:
            gameWolrd.remove_object(self)

    def getHitBox(self):
        return self.x + 145, self.y + 70, self.x + 245, self.y + 160

    def drawHitBox(self):
        x1, y1, x2, y2 = self.getHitBox()
        points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        pygame.draw.polygon(gameWolrd.screen, (0, 0, 0), points, 1)

    def collision(self, type, other):
        if type == "bulletToMonster":
            self.hp -= other.getDamage()
            if self.hp <= 0:
                gameWolrd.remove_object(self)
                gameWolrd.score += 10
        if type == "PlayerToMonster":
            gameWolrd.remove_object(self)


delay = 0
def addMoster():
    global delay
    if delay == 0:
        while True:
            Pattern = []
            for _ in range(5):
                Pattern.append(random.randint(0,2))
            if 1 in Pattern or 2 in Pattern: # 1또는 2가 한 번도 안나오는 경우가 생길 수 있기 때문에 체크를 함.
                break
        for index, value in enumerate(Pattern):
            if not value == 0:
                gameWolrd.add_object(Monster(index * 125, -200, 100 * (1 + (gameWolrd.score / 1000))), 2)

    delay = (delay + 1) % 100




