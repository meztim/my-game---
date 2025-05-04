import pygame

class Picture:
    def__init__(self, image, w, h, x, y, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.image = transform.scale(image.load(image_),(w, h))
        self.w = w
        seelf.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        screen.blit(self.image,(self.x, self.y))

class Platform1(Picture):
    def_init__(self, image, w, h, color, x, y):
        super().__init__(image, w, h, x, y)
        self.color = color

    def move(self):
        if keys[K_UP] and self.rect.y != 10:
            self.rect.y -= self.speed
        if keys[k_DOWN] and self.rect.y != 490:
            self.rect.y += self.speed

class Platform2(Picture):
    def_init__(self, image, w, h, x, y):
        super().__init__(image, w, h, x, y

    def move(self):
        if keys[K_w] and self.rect.x != 10:
            self.rect.y -= self.speed
        if keys[k_DOWN] and self.rect.y != 490:
            self.rect.y += self.speed

class Boll(Picture):
    def_init__(self, image, w, h, x, y):
        super().__init__(image, w, h, x, y)
        self.speed_x = self.speed
        self.speed_y = self. speed

    def colliderect(self,rect):
        if self.rect.colliderect(rect):
            self.speed_y *= - 1
        elif boll.rect.x == platform1.rect.x :
            self.speed_x *= - 1
        if boll.rect.x == 700:
            boll.rect.x == 700
            self.speed_y *= -1



window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('YU69WYqi1Vg.jpg'),(700,500))

#создание объктов игры
boll = Boll('wimbledon.crop_642x481_0,7.preview.jpg', 65, 65, 330, 180, 5 )
platform1 = Platform1('8a3e58af9aebd6aad8c51f6c9d8fdfcd.jpg', 30, 100, 40, 150, 5 )
platform2 = Platform2('d8e9f9afeae4571b6d3427115de34f45.jpg', 30, 100, 660, 150, 5)
