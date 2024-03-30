import pygame

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()

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

platform_left = Player('pngegg.png', 0, 100, 4, 30, 150)
platform_right = Player('pngegg.png', 670, 100, 4, 30, 150)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    window.fill((234,234,234))
    platform_left.reset()
    platform_left.update_left()
    platform_right.reset()
    platform_right.update_right()
    clock.tick(60)
    pygame.display.update()