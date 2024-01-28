import pygame
from random import randint
class CHAMA:
    def __init__(self):
        palito = pygame.image.load("palito.png").convert_alpha()
        self.surf = pygame.transform.scale_by(palito, 2)

        self.particulas = []
        self.index = len(self.particulas)
        self.cor = 'white'
        self.timer = 60
        self.vel = 0
    
    def adicionar(self):
        x = pygame.mouse.get_pos()[0] - self.surf.get_width() + 15
        y = pygame.mouse.get_pos()[1] - self.surf.get_height() + 20
        raio = 11
        dir_x = randint(-1, 1)
        dir_y = randint(-3, -1)
        particula_circulo = [[x, y], raio, [dir_x, dir_y]]
        self.particulas.append(particula_circulo)

    def deletar_particulas(self):
        particas_copy = [p for p in self.particulas if p[1] > 0]
        self.particulas = particas_copy

    def draw(self, tela):
        x = pygame.mouse.get_pos()[0] - self.surf.get_width() + 10
        y = pygame.mouse.get_pos()[1] - self.surf.get_height()  + 20
        tela.blit(self.surf, (x, y))
        if self.particulas:
            for p in self.particulas:
                p[0][0] -= p[2][0]  #x
                p[0][1] += p[2][1] - self.vel#y
                p[1] -= 0.2
                
                if p[1] >= 10:
                    self.cor = 'white'
                if p[1] <= 9:
                    self.cor = 'yellow'
                    p[0][0] += randint(-1, 1)
                if p[1] <= 8:
                    self.cor = 'red'
                    p[0][0] += p[2][0] 
                    p[0][0] += randint(-2, 2) 
                if p[1] <= 5:
                    self.cor = 'black'
                    p[0][0] += p[2][0] 
                    p[0][0] += randint(-1, 1)                 
                pygame.draw.circle(tela, self.cor, p[0], int(p[1]))
                
    def update(self, tela):
        self.adicionar()
        self.deletar_particulas()
        self.draw(tela)