from abc import ABC, abstractmethod

# Producto: Interfaz común para todos los vehículos
class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

# Productos concretos
class Auto(Vehiculo):
    def conducir(self):
        print("Conduciendo un auto")

class Moto(Vehiculo):
    def conducir(self):
        print("Conduciendo una moto")

# Creador: Define el método fábrica abstracto
class VehiculoFactory(ABC):
    @abstractmethod
    def crear_vehiculo(self):
        pass

# Creadores concretos
class AutoFactory(VehiculoFactory):
    def crear_vehiculo(self):
        return Auto()

class MotoFactory(VehiculoFactory):
    def crear_vehiculo(self):
        return Moto()

# Cliente
if __name__ == "__main__":
    auto_factory = AutoFactory()
    auto = auto_factory.crear_vehiculo()
    auto.conducir()  # Salida: Conduciendo un auto

    moto_factory = MotoFactory()
    moto = moto_factory.crear_vehiculo()
    moto.conducir()  # Salida: Conduciendo una moto
