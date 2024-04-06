import pygame
import random
import time
pygame.mixer.init()
pygame.init()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()
sound1 = pygame.mixer.Sound('zvuk-udara-po-myachiku.ogg')
pygame.mixer.music.load('60655cdca47ed56e7802f58.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_left(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y + self.rect.height < 500:
            self.rect.y += self.speed
    def update_right(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y + self.rect.height < 500:
            self.rect.y += self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed_x, speed_y, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
    def update_ball(self, platform_left, platform_right):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.colliderect(platform_left) or self.rect.colliderect(platform_right):
            self.speed_x *= -1
            sound1.play()
        if self.rect.y < 0 or self.rect.y > 500 - self.height:
            self.speed_y *= -1
            sound1.play()
        window.blit(self.image, (self.rect.x, self.rect.y))
    def is_lose(self):
        if self.rect.x > 700 - self.width:
            return 'right'
        elif self.rect.x < 0:
            return 'left'
        else:
            return 'not'

platform_left = Player('pngegg.png', 0, 100, 4, 30, 150)
platform_right = Player('pngegg.png', 670, 100, 4, 30, 150)
ball = Ball('pngegg (1).png', 330, 250, 4, 4, 50, 50)

start = time.time()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    if ball.is_lose() == 'not':
        window.fill((128,128,128))
        platform_left.reset()
        platform_left.update_left()
        platform_right.reset()
        platform_right.update_right()
        ball.update_ball(platform_left.rect, platform_right.rect)
        pygame.draw.line(window, (255, 255, 255), [350, 0], [350, 500], 5)
        clock.tick(60)
        pygame.display.update()
    else:
        #end = time.time()
        if ball.is_lose() == 'left':
            f1 = pygame.font.Font(None, 60)
            text1 = f1.render('Правый выйграл!', True, (225, 225, 225))
        if ball.is_lose() == 'right':
            f1 = pygame.font.Font(None, 60)
            text1 = f1.render('Левый выйграл!', True, (225, 225, 225))
            #text2 = f1.render(str(int(end-start)), True, (225, 225, 225))
        window.blit(text1, (210, 200))
        #window.blit(text2, (350, 250))
        pygame.display.update()
pygame.display.update() 