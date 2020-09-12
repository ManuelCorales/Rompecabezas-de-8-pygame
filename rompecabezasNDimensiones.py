import pygame
import math
from juego.generarRompecabezas import GenerarRompecabezas
import time

class Rompecabezas:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.dist = 200
        self.clock = pygame.time.Clock()
        print("Ingrese las dimensiones deseadas")
        self.dimensiones = int(input())
        self.pantalla = pygame.display.set_mode((self.dimensiones * 150 , self.dimensiones * 150))
        pygame.display.set_caption('Rompecabezas')
        self.pantalla.fill(self.black)
        self.generarRompecabezas = GenerarRompecabezas(self.pantalla, self.dimensiones)


    def empezar(self):
        self.numerosRompecabezas = self.generarRompecabezas.generarRompecabezas()
        self.generarRompecabezas.dibujarRompezabezas(self.numerosRompecabezas)

        self.finish = False
        self.you_win = False
        while not self.finish:
            # if(not self.you_win):
            for event in pygame.event.get():
                    self.you_win = True
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        self.finish = True

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        clickDeMouse = pygame.mouse.get_pos()
                        indexElegido = -1
                        for i in range(self.dimensiones):
                            for j in range(self.dimensiones):
                                if(clickDeMouse[0] <= (150 * (j + 1)) and clickDeMouse[1] <= (150 * (i + 1))):
                                    indexElegido = j + (i * self.dimensiones)
                                    break
                            if indexElegido != -1:
                                break
                        if(self.esSwapeable(self.numerosRompecabezas, indexElegido)):
                            self.numerosRompecabezas[self.numerosRompecabezas.index(self.dimensiones ** 2)], self.numerosRompecabezas[indexElegido] = self.numerosRompecabezas[indexElegido], self.numerosRompecabezas[self.numerosRompecabezas.index(self.dimensiones ** 2)]
                            self.generarRompecabezas.dibujarRompezabezas(self.numerosRompecabezas)
                            for i in range((self.dimensiones ** 2) - 1):
                                if(self.numerosRompecabezas[i] is not (i + 1)):
                                    self.you_win = False
                                    break
                            if(self.you_win):
                                pygame.display.set_caption('YOU WIN GANASTE')
                                self.pantalla.fill(self.black)
                                letra_win = pygame.font.SysFont('Comic Sans MS', 40)
                                texto = letra_win.render("YOU WIN GANASTE", True, (152, 251, 152))
                                self.pantalla = pygame.display.set_mode((450, 450))
                                self.pantalla.blit(texto, (30, 200))
                                pygame.display.update()
                                time.sleep(5)
                                pygame.quit()
                                quit()

            pygame.display.update()

    def esSwapeable(self, arrayNumeros, indexElegido):
        indexNueve = arrayNumeros.index(self.dimensiones ** 2)
        if (abs(indexElegido - indexNueve) == self.dimensiones or abs(indexElegido - indexNueve) == 1):
            if ((indexNueve % self.dimensiones == 0 and indexElegido == indexNueve - 1) or ((indexNueve + 1) % self.dimensiones == 0 and indexElegido == indexNueve + 1)):
                return False
            return True
        else:
            return False





if __name__ == "__main__":
    rompecabezas = Rompecabezas()
    rompecabezas.empezar()