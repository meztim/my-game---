from pygame import *
from random import *


class Picture:
    def __init__(self, image_, w, h, x, y, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.image = transform.scale(image.load(image_),(w, h))
        self.w = w
        self.h = h
        self.rect = Rect(self.x, self.y, self.w, self.h)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        screen.blit(self.image,(self.x, self.y))

class Platform1(Picture):
    def __init__(self, image, w, h, x, y, speed):
        super().__init__(image, w, h, x, y, speed)
        self.color = color

    def move(self, keys):
        if keys[K_w] and self.rect.y != 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y != 490:
            self.rect.y += self.speed
        if self.rect.y <= 5 :
            self.rect.y = 5
        elif self.rect.y >= 395:
            self.rect.y = 395

class Platform2(Picture):
    def __init__(self, image, w, h, x, y, speed):
        super().__init__(image, w, h, x, y, speed)

    def move(self, keys):
        if keys[K_UP] and self.rect.x != 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y != 490:
            self.rect.y += self.speed
        if self.rect.y <= 5 :
            self.rect.y = 5
        elif self.rect.y >= 395:
            self.rect.y = 395

class Boll(Picture):
    def __init__(self, image, w, h, x, y, speed, speedx, speedy):
        super().__init__(image, w, h, x, y, speed)
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        global a, b
        self.rect.x -= self.speedx
        self.rect.y -= self.speedy
        if self.rect.colliderect(platform1.rect):
            self.speedx = -self.speedx
        elif self.rect.y <= 0  :
            self.speedy = -self.speedy
        elif self.rect.colliderect(platform2.rect):
            self.speedx = -self.speedx
        elif self.rect.y >= 435:
            self.speedy = -self.speedy
        if boll.rect.x <= -65:
            boll.rect.x = 285
            boll.rect.y = 185
            a += 1
        elif boll.rect.x >= 765:
            boll.rect.x = 285
            boll.rect.y = 185
            b += 1


window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('6458324097.jpg'),(700,500))

#создание объктов игры
boll = Boll('New Piskel.png', 65, 65, 330, 180, 5, randint(2,4), randint(2,4))
platform1 = Platform1('8a3e58af9aebd6aad8c51f6c9d8fdfcd.jpg', 30, 100, 40, 150, 6)
platform2 = Platform2('d8e9f9afeae4571b6d3427115de34f45.jpg', 30, 100, 660, 150, 6)
#Настрока частоты обновления экрана
clock = time.Clock()
FPS = 60

#текс
font.init()
my_font = font.SysFont(None, 80)
text_ska = my_font.render('скала выйграла', True, (78, 194, 54))
text_gor = my_font.render('гора выйграла', True, (117, 0, 0))


#текс игры
font.init()
font = font.SysFont(None, 30)
text1 = 'Счёт:'
text2 = 'Cчет:'


code = 0

a = 0
b = 0



game = True
while game:
    #Обработчик событий
    for e in event.get():
        if e.type == QUIT:
            game = False
    if code == 0:
        keys = key.get_pressed()
        platform1.move(keys)
        platform2.move(keys)

        #отрисовка
        window.blit(background,(0,0))
        boll.reset()
        boll.update()
        platform1.reset()
        platform2.reset()

        surface = font.render(text2 + str(b), True, (0, 255, 255))
        window.blit(surface, (30, 30))

        surface1 = font.render(text1 + str(a), True, (0, 255, 255))
        window.blit(surface1, (610, 30))

        if a >= 3:
            code = 1
        if b >= 3:
            code = 2

    if code == 1:
        window.blit(text_gor,(145,225))
    if code == 2 :
        window.blit(text_ska, (145, 225))


    #Обновление экрана
    display.update()
    clock.tick(FPS)