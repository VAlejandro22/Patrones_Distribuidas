from abc import ABC, abstractmethod

# Producto Vehiculo
class Vehiculo(ABC):
    @abstractmethod
    def crear(self):
        pass

# Producto Accesorio
class Accesorio(ABC):
    @abstractmethod
    def instalar(self):
        pass

# Clases concretas de Vehiculo
class Auto(Vehiculo):
    def crear(self):
        print("Creando un auto")

class Moto(Vehiculo):
    def crear(self):
        print("Creando una moto")

# Clases concretas de Accesorio
class Rueda(Accesorio):
    def instalar(self):
        print("Instalando una rueda")

class Motor(Accesorio):
    def instalar(self):
        print("Instalando un motor")

# Fábrica abstracta
class VehiculoFactory(ABC):
    @abstractmethod
    def crear_vehiculo(self) -> Vehiculo:
        pass

    @abstractmethod
    def crear_accesorio(self) -> Accesorio:
        pass

# Fábrica concreta para vehículos y accesorios de autos
class AutoFactory(VehiculoFactory):
    def crear_vehiculo(self) -> Vehiculo:
        return Auto()

    def crear_accesorio(self) -> Accesorio:
        return Rueda()

# Fábrica concreta para vehículos y accesorios de motos
class MotoFactory(VehiculoFactory):
    def crear_vehiculo(self) -> Vehiculo:
        return Moto()

    def crear_accesorio(self) -> Accesorio:
        return Motor()

# Uso del patrón Abstract Factory
if __name__ == "__main__":
    # El cliente elige qué tipo de fábrica usar
    auto_factory = AutoFactory()
    auto = auto_factory.crear_vehiculo()
    rueda = auto_factory.crear_accesorio()

    auto.crear()  # Salida: Creando un auto
    rueda.instalar()  # Salida: Instalando una rueda

    print()

    moto_factory = MotoFactory()
    moto = moto_factory.crear_vehiculo()
    motor = moto_factory.crear_accesorio()

    moto.crear()  # Salida: Creando una moto
    motor.instalar()  # Salida: Instalando un motor
