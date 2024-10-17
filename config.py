import pygame
import time
import os
from Player import *
from Apple import *


class Game:
    game_height = 800
    game_width = 1200
    score = 0
    #rotar1 = pygame.transform.rotate("cuare2.png", 45)
    
    def __init__(self):

        self._running = True
        self.myfont = None
    def scorePlus(self):
        self.score += 100

    def on_init(self):
        pygame.init()
        pygame.font.init() #Inicializa la fuente para poder escribir puntajes
        self.myfont = pygame.font.SysFont("monospace", 36, True, True)
        self.player = Player()
        self.apple = Apple()
        self._display_surf = pygame.display.set_mode((self.game_width,self.game_height), pygame.HWSURFACE)

        """pygame.display.set_caption("Viborota")
        img_folder = os.path.join(os.path.dirname(__file__), 'img')  
        self._flag_img = pygame.image.load(os.path.join(img_folder, "cuare2.png")).convert()  
        self._apple_img = pygame.image.load(os.path.join(img_folder, "apple2.png")).convert()"""

        img_folder = os.path.join(os.path.dirname(__file__), 'img')  
        original_img = pygame.image.load(os.path.join(img_folder, "cuare2.png")).convert_alpha()  # Usar convert_alpha para imágenes con transparencia  
        self._flag_img = pygame.transform.rotate(original_img, self.player.cambio_movimiento())  # Rota la imagen 45 grados  
        self._apple_img = pygame.image.load(os.path.join(img_folder, "apple2.png")).convert_alpha()
         

    
    def on_render(self):
        self._display_surf.fill((0,0,0))

# dibujo 4 rectangulos para limites. La disposicion de los parametros esta en orden de primero a cuarto (der, abajo, arriba, izq)
# Las coordenadas y dimensiones del rectángulo, que también se especifican como una tupla de cuatro valores: (x, y, ancho, alto).
        pygame.draw.rect(self._display_surf, (0,255,0), (self.game_width - 10,0,10,self.game_height)) #Derecha
        pygame.draw.rect(self._display_surf, (0,255,0), (0,self.game_height - 10,self.game_width,10)) #abajo
        pygame.draw.rect(self._display_surf, (0,255,0), (0,0,self.game_width,10)) #arriba
        pygame.draw.rect(self._display_surf, (0,255,0), (0,0,10,self.game_height)) #izquierda

        self._display_surf.blit(self._flag_img, (self.player.x, self.player.y))
        self._display_surf.blit(self._apple_img, (self.apple.randx, self.apple.randy))
        scoretext = self.myfont.render("Score = "+str(self.score), 1, (200,255,255))
        self._display_surf.blit(scoretext, (800, 10))
        for pos in self.player.positions:
            self._display_surf.blit(self._flag_img, (pos[0],pos[1]))
        
        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        speedup = 0.200
        if self.on_init() == False:
            self._running = False
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False


            self.player.movimiento()
            if len(self.player.positions) < self.player.lenght:
                self.player.positions.append((self.player.x, self.player.y))
            else:
                self.player.positions.pop(0)
                self.player.positions.append((self.player.x, self.player.y))
            
            if self.apple.comerManzana(self.player.x, self.player.y, self.apple.randx, self.apple.randy, 40):
                self.apple.nuevaManzana()
                self.player.lenght +=1
                self.scorePlus()
                if speedup > 0.100:
                    speedup -= 0.025
            

            self.on_render()
            time.sleep(speedup)


        self.on_cleanup()
