import pygame
from sys import exit
from particulas import CHAMA
pygame.init()

tela = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

p = CHAMA()

while True:
    tela.fill('gray20')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    p.update(tela)
    pygame.display.flip()
    clock.tick(60)