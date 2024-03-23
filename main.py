import pygame

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    window.fill((234,234,234))
    clock.tick(60)
    pygame.display.update()