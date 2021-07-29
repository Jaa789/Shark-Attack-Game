import pygame
from pygame.locals import *
import os
import random
import time

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()

info = pygame.display.Info()
if info.current_h <= 768:
    W, H = info.current_w, info.current_h - y
elif info.current_h > 768:
    W, H = info.current_w, 768 - y

win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Shark Attack Game')
pygame.display.update()

bg = pygame.image.load(os.path.join('images', 'mybg.png')).convert_alpha()
bgX = 0
bgX2 = bgX + bg.get_width()

clock = pygame.time.Clock()

class player(object):
    transparent = (0, 0, 0, 0)
    run = [pygame.image.load(os.path.join('images', 'Shark (1)' + '.png')).convert_alpha()]
    run2 = [pygame.image.load(os.path.join('images', 'Shark (1)' + '.png')).convert_alpha()]
    run[0].fill(transparent)


    fall = [pygame.image.load(os.path.join('images', 'Shark (2).png')).convert_alpha()]
    fall2 = [pygame.image.load(os.path.join('images', 'Shark (2).png')).convert_alpha()]
    fall[0].fill(transparent)

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.falling = False

    def draw(self, win):
        if self.falling == True:
            win.blit(self.run[0], (self.x, self.y))
            win.blit(self.fall2[0], (self.x, self.y))
            pygame.time.set_timer(USEREVENT+ 4, 500)

        elif self.falling == False:
            win.blit(self.fall[0], (self.x, self.y))
            win.blit(self.run2[0], (self.x, self.y))
        self.hitbox = pygame.Rect(self.x + 540, self.y + 130, self.run2[0].get_rect().width - 650, self.run2[0].get_rect().height - 230)
        #pygame.draw.rect(win, (0,0,0),self.hitbox, 2)

class yellow(object):
    yelfish = [pygame.image.load(os.path.join('images', 'Fish (1).png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4

    def draw(self, win):
        fish_1 = self.yelfish[0]
        self.hitbox = pygame.Rect(self.x, self.y, fish_1.get_rect().width, fish_1.get_rect().height)
        #pygame.draw.rect(win, (0,0,0), self.hitbox, 2)
        win.blit(self.yelfish[0], (self.x,self.y))

    def collide(self, rect):
        coll = self.hitbox.colliderect(rect)
        return(coll)

class red(object):
    redfish = [pygame.image.load(os.path.join('images', 'Fish (2).png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4

    def draw(self, win):
        fish_2 = self.redfish[0]
        self.hitbox = pygame.Rect(self.x, self.y, fish_2.get_rect().width, fish_2.get_rect().height)
        #pygame.draw.rect(win, (0,0,0), self.hitbox, 2)
        win.blit(self.redfish[0], (self.x,self.y))

    def collide(self, rect):
        coll = self.hitbox.colliderect(rect)
        return(coll)


class purple(object):
    purfish = [pygame.image.load(os.path.join('images', 'Fish (3).png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4

    def draw(self, win):
        fish_3 = self.purfish[0]
        self.hitbox = pygame.Rect(self.x, self.y, fish_3.get_rect().width, fish_3.get_rect().height)
        #pygame.draw.rect(win, (0,0,0), self.hitbox, 2)
        win.blit(self.purfish[0], (self.x,self.y))

    def collide(self, rect):
        coll = self.hitbox.colliderect(rect)
        return(coll)


class orange(object):
    orafish = [pygame.image.load(os.path.join('images', 'Fish (4).png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4

    def draw(self, win):
        fish_4 = self.orafish[0]
        self.hitbox = pygame.Rect(self.x, self.y, fish_4.get_rect().width, fish_4.get_rect().height)
        #pygame.draw.rect(win, (0,0,0), self.hitbox, 2)
        win.blit(self.orafish[0], (self.x,self.y))

    def collide(self, rect):
        coll = self.hitbox.colliderect(rect)
        return(coll)


def updateFile():
    f = open('scores.txt','r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score

    return last


def redrawWindow():
    largeFont = pygame.font.SysFont('comicsans', 30)
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2,0))
    text = largeFont.render('Score: ' + str(score), 1, (255,255,255))
    runner.draw(win)
    for obstacle in obstacles:
        obstacle.draw(win)

    win.blit(text, (700, 10))
    pygame.display.update()


fast = 0

pygame.time.set_timer(USEREVENT+ 1, 1000)
stop = 500 - fast*1000
if stop > 100:
    pygame.time.set_timer(USEREVENT+ 2, stop)
elif stop <= 100:
    pygame.time.set_timer(USEREVENT+ 2, 100)


def move_screen():
    global bgX, bgX2, fast
    stop = (4 + fast - 0.2)
    if stop <= 9:
        bgX = (bgX - stop) % bg.get_width()
    if stop > 9:
        bgX = (bgX - 9) % bg.get_width()
    bgX2 = bgX - bg.get_width()

speed = 180

score = 0

run = True
runner = player(-300, 150, 64, 64)

obstacles = []
pause = 0
fallSpeed = 0

while run:
    move_screen()
    for obstacle in obstacles:
        if obstacle.collide(runner.hitbox):
            runner.falling = True
            obstacles.pop(obstacles.index(obstacle))
            score += 1

        if obstacle.x < -128:
            obstacles.pop(obstacles.index(obstacle))
        else:
            if (4 + fast - 0.1) <= 15:
                obstacle.x -= (4.2 + fast - 0.1)
            if (4.2 + fast - 0.1) > 15:
                obstacle.x -= 15

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

        if event.type == USEREVENT+1:
            fast += 0.1

        if event.type == USEREVENT+2:
            r = random.randrange(4)
            ry = random.randrange(30, H - 100)
            if r == 0:
                obstacles.append(yellow(1600, ry, 64, 64))
            elif r == 1:
                obstacles.append(red(1600, ry, 64, 64))
            elif r == 2:
                obstacles.append(purple(1600, ry, 64, 64))
            elif r == 3:
                obstacles.append(orange(1600, ry, 64, 64))

        if event.type == USEREVENT+4:
            runner.falling = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        runner.y -= 2
    if keys[pygame.K_RIGHT]:
        runner.x += 2
    if keys[pygame.K_LEFT]:
        runner.x -= 2
    if keys[pygame.K_DOWN]:
        runner.y += 2

    clock.tick(speed)
    redrawWindow()
