import pygame


class BotonNumero():
    def __init__(self, pantalla, numero, dimensiones, pos_x=0, pos_y=0 ):
        self.pantalla = pantalla
        self.fuente = pygame.font.SysFont('Comic Sans MS', 25)
        self.sqr_side = 148
        self.rectangulo = pygame.draw.rect(self.pantalla, (122, 173, 255), (pos_x, pos_y, self.sqr_side, self.sqr_side))
        if numero != dimensiones:
            self.texto_a_pantalla(numero, pos_x + 65, pos_y + 50)

    def texto_a_pantalla(self, texto, x, y):
        texto = str(texto)
        self.textsurface = self.fuente.render(texto, True, (0, 56, 145))
        self.pantalla.blit(self.textsurface, (x, y))
