import pygame
from config import *
class Player:
    x = 0
    y = 0
    d = 0
    direccion = 0

    positions = []
    lenght = 5

    def movimiento(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT]):
                self.d = 0
                
        if (keys[pygame.K_LEFT]):
                self.d = 1
        if (keys[pygame.K_UP]):
                self.d = 2 
        if (keys[pygame.K_DOWN]):
                self.d = 3
                self.direccion = 45

        if self.d == 0:
                self.x += 40
        elif self.d == 1:
                self.x -= 40
        elif self.d == 2:
                self.y -= 40
        elif self.d == 3:
                self.y += 40
        else:
                pass

    def cambio_movimiento(self):
        #self.nueva_direccion = 0
        self.nueva_direccion = self.direccion
        return self.nueva_direccion




