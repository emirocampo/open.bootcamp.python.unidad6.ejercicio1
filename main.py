class Vehiculo:
    color = "azul"
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):
    velodidad = 220
    cilindrada = 2500

coche = Coche()
print("color: ",coche.color)
print("ruedas: ",coche.ruedas)
print("puertas: ",coche.puertas)
print("velocidad max: ",coche.velodidad)
print("cilindraje: ",coche.cilindrada)