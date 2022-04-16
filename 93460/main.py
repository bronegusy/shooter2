from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (100, 100))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_w - 80:
            self.rect.x += self.speed
    def shoot(self):
        bullet = Bullet('bullet.png', self.rect.x + 15, self.rect.y, 5)
        bullets.append(bullet)


class Enemy(GameSprite):

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_h:
            self.rect.y = -10
            self.rect.x = randint(50, win_w - 50)

class Enemy2(GameSprite):

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_h:
            self.rect.y = -10
            self.rect.x = randint(50, win_w - 50)

class Enemy3(GameSprite):

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_h:
            self.rect.y = -10
            self.rect.x = randint(50, win_w - 50)

class Enemy4(GameSprite):

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_h:
            self.rect.y = -10
            self.rect.x = randint(50, win_w - 50)

class Enemy5(GameSprite):

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_h:
            self.rect.y = -10
            self.rect.x = randint(50, win_w - 50)

class Bullet(GameSprite):

    def update(self):
        self.rect.y -= self.speed


win_w, win_h = 700, 500
window = display.set_mode((win_w, win_h))
background = transform.scale(image.load("fon.jpg"), (700, 500))
player = Player("player.png", 300, 400,  5)
enemy = Enemy('w.png', randint(50, win_w - 0), -50, randint(1, 3))
enemy2 = Enemy2('w.png', randint(50, win_w - 10), -50, randint(1, 3))
enemy3 = Enemy2('w.png', randint(50, win_w - 20), -50, randint(1, 3))
enemy4 = Enemy2('w.png', randint(50, win_w - 30), -50, randint(1, 3))
enemy5 = Enemy2('w.png', randint(50, win_w - 40), -50, randint(1, 3))
bullets = list()

mixer.init()
mixer.music.load("key.mp3")
mixer.music.play()

timer = time.Clock()
fps = 60

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.shoot()
    if not finish:
        window.blit(background, (0, 0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        enemy2.update()
        enemy2.reset()
        enemy3.update()
        enemy3.reset()
        enemy4.update()
        enemy4.reset()
        enemy5.update()
        enemy5.reset()
        display.update()
    timer.tick(fps)