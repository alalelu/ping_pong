import pygame

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.speed = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    window.fill((234,234,234))
    clock.tick(60)
    pygame.display.update()