import pickle


class Vehiculo:
    def __init__(self, color, ruedas, puertas) :
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) -> str:
        return (f"color: {self.color}, número de ruedas: {self.ruedas}, número de puertas: {self.puertas}, velocidad maxima: {self.velocidad}, cilindraje: {self.cilindrada}")

# m = Coche("Verde", 4, 5, 180, 2600)
# f = open('Vehiculo.bin', 'wb')
# pickle.dump(m, f)
# f.close()

f = open('Vehiculo.bin', 'rb')
m = pickle.load(f)
f.close()

print(m)