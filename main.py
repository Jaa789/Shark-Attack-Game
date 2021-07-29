import pygame
from pygame.locals import *
import os
import random

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()


info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
if info.current_h <= 768:
    W, H = info.current_w, info.current_h - y
elif info.current_h > 768:
    W, H = info.current_w, 768 - y

win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Shark Attack Game')
pygame.display.update()

bg = pygame.image.load(os.path.join('images', 'mybg.png')).convert()
bgX = 0
bgX2 = bgX + bg.get_width()

clock = pygame.time.Clock()

class player(object):
    run = [pygame.image.load(os.path.join('images', 'Shark (1)' + '.png'))]
    jump = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png'))]
    for i in range(1, 8):
        slide.append(pygame.image.load(os.path.join('images', 'S2.png')))
    for x in range(3, 6):
        slide.append(pygame.image.load(os.path.join('images', 'S{}.png'.format(x))))
    fall = pygame.image.load(os.path.join('images', 'Shark (2).png'))
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]


    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.falling = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.falling:
            win.blit(self.fall, (self.x, self.y + 30))
        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.3
            win.blit(self.jump[self.jumpCount//18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
                self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            elif self.slideCount > 20 and self.slideCount < 80:
                self.hitbox = (self.x, self.y+3, self.width-8, self.height-35)

            if self.slideCount >= 110:
                self.slideCount = 0
                self.runCount = 0
                self.slideUp = False
                self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-10)
            win.blit(self.slide[self.slideCount//10], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.run:
                win.blit(self.run[0], (self.x,self.y))
                self.hitbox = (self.x+ 4, self.y, self.width-24, self.height-13)

        #pygame.draw.rect(win, (255,0,0),self.hitbox, 2)

class yellow(object):
    yelfish = [pygame.image.load(os.path.join('images', 'Fish (1).png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.yelfish[0], (self.x,self.y))

    """ def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False """

class red(object):
    redfish = [pygame.image.load(os.path.join('images', 'Fish (2).png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.redfish[0], (self.x,self.y))

    """ def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False """

class purple(object):
    purfish = [pygame.image.load(os.path.join('images', 'Fish (3).png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.purfish[0], (self.x,self.y))

    """ def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False"""

class orange(object):
    orafish = [pygame.image.load(os.path.join('images', 'Fish (4).png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1.4

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.orafish[0], (self.x,self.y))

    """def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False"""



""" class spike(saw):
    img = pygame.image.load(os.path.join('images', 'spike.png'))

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y, 28,315)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False """


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



def endScreen():
    global pause, score, speed, obstacles
    pause = 0
    speed = 30
    obstacles = []

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                runner.falling = False
                runner.sliding = False
                runner.jumpin = False

        win.blit(bg, (0,0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        lastScore = largeFont.render('Best Score: ' + str(updateFile()),1,(255,255,255))
        currentScore = largeFont.render('Score: '+ str(score),1,(255,255,255))
        win.blit(lastScore, (W/2 - lastScore.get_width()/2,150))
        win.blit(currentScore, (W/2 - currentScore.get_width()/2, 240))
        pygame.display.update()
    score = 0

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
pygame.time.set_timer(USEREVENT+ 3, 1000)



def move_screen():
    global bgX, bgX2, fast
    stop = (4 + fast - 0.2)
    if stop <= 9:
        bgX = (bgX - stop) % bg.get_width()
    if stop > 9:
        bgX = (bgX - 9) % bg.get_width()
    bgX2 = bgX - bg.get_width()

speed = 120

score = 0

run = True
runner = player(-300, 150, 64, 64)

obstacles = []
pause = 0
fallSpeed = 0

while run:
    if pause > 0:
        pause += 1
        if pause > fallSpeed * 2:
            endScreen()

    for obstacle in obstacles:
        """if obstacle.collide(runner.hitbox):
            runner.falling = True

            if pause == 0:
                pause = 1
                fallSpeed = speed"""
        if obstacle.x < -128:
            obstacles.pop(obstacles.index(obstacle))
        else:
            if (4 + fast - 0.1) <= 15:
                obstacle.x -= (4.2 + fast - 0.1)
            if (4.2 + fast - 0.1) > 15:
                obstacle.x -= 15


    move_screen()

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

        if event.type == USEREVENT+3:
            score += 1


    if runner.falling == False:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if not(runner.jumping):
                runner.jumping = True

        if keys[pygame.K_DOWN]:
            if not(runner.sliding):
                runner.sliding = True

    clock.tick(speed)
    redrawWindow()
