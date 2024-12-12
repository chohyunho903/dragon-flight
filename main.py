from operator import truediv

import pygame
from pygame.time import delay

import Background
import Monster
import gameWolrd

import Player



def init():
    global leifMouseEventCheck
    global mousePos, clock
    global player
    global font

    gameWolrd.running = True
    pygame.init()
    font = pygame.font.SysFont(None, 36)  # 시스템 폰트, 크기 36

    leifMouseEventCheck = False
    mousePos = (gameWolrd.screen_width/2,0)
    clock = pygame.time.Clock()
    player = Player.Player(gameWolrd.screen_width / 2, 700)
    gameWolrd.add_object(player, 1)
    gameWolrd.add_object(Background.Background(0,0))
    gameWolrd.add_object(Background.Background(0, -gameWolrd.screen_height))
    gameWolrd.add_object(Background.Background(0, -(gameWolrd.screen_height * 2 )))


init()
while gameWolrd.running:
    global event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 종료
            gameWolrd.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 왼쪽 클릭
                leifMouseEventCheck = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # 왼쪽 클릭
                leifMouseEventCheck = False

        if event.type == pygame.MOUSEMOTION:
            if leifMouseEventCheck:
                mousePos = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.useSkill()




    gameWolrd.updata(mousePos)
    gameWolrd.render()
    Monster.addMoster()
    gameWolrd.updateCollision()

    # 점수 출력
    text = font.render("Score : " + str(gameWolrd.score), True, (255, 255, 255))
    gameWolrd.screen.blit(text, (10, 10))  # (100, 100) 위치에 출력

    # 플레이어 HP 출력
    text = font.render("Player Life : " + str(player.getPlayerHp()), True, (255, 255, 255))
    gameWolrd.screen.blit(text, (10, 35))  # (100, 100) 위치에 출력

    pygame.display.update()
    clock.tick(60)

if not event.type == pygame.QUIT:
    delay(3000)
