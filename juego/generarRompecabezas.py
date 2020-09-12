import random
from juego.botonNumero import BotonNumero


class GenerarRompecabezas:
    def __init__(self, pantalla, dimensiones):
        self.pantalla = pantalla
        self.digitos = []
        self.dimensiones = dimensiones ** 2

    def generarRompecabezas(self):
        del self.digitos[:]
        while len(self.digitos) != self.dimensiones:
            num = random.randint(1, self.dimensiones)
            if num not in self.digitos:
                self.digitos.append(num)
        return self.digitos

    def dibujarRompezabezas(self, numeros):
        counter_x = 0
        counter_y = 0
        rompecabezas = []
        for numero in numeros:
            rompecabezas.append(BotonNumero(self.pantalla, numero, self.dimensiones, 150 * counter_x, 150 * counter_y))
            counter_x += 1
            if counter_x % self.dimensiones**0.5 == 0:
                counter_x = 0
                counter_y += 1

        return rompecabezas