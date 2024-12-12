import pygame

running = False
screen_width = 600
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
GameWorld = [[] for _ in range(4)] # 레이어 구별 0: 배경, 1: 플레이어, 2: 몬스터, 3:블릿
score = 0 # 점수

# 게임 월드에 객체 담기
def add_object(o, depth=0):
    GameWorld[depth].append(o)

# 게임 월드 객체들을 모두 업데이트 하기
def updata(pos):
    for layer in GameWorld:
        for o in layer:
            o.update(pos)


# 게임 월드 객체들을 모두 그리기
def render():
    for layer in GameWorld:
        for o in layer:
            o.draw()


# 객체 삭제
def remove_object(o):
    for layer in GameWorld:
        if o in layer:
            layer.remove(o)
            del o
            return

# 충돌처리
def collide(a, b):
    la, ba, ra, ta = a.getHitBox()
    lb, bb, rb, tb = b.getHitBox()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True

def checkBulletToMonsterCollision():
    for b in GameWorld[3]: # 블릿
        for m in GameWorld[2]: # 몬스터
            if collide(b, m):
                b.collision("bulletToMonster",m)
                m.collision("bulletToMonster", b)

def checkPlayerToMonsterCollision():
    for p in GameWorld[1]: # 플레이어
        for m in GameWorld[2]: # 몬스터
            if collide(p, m):
                p.collision("PlayerToMonster",m)
                m.collision("PlayerToMonster",p)

def updateCollision():
    checkBulletToMonsterCollision()
    checkPlayerToMonsterCollision()