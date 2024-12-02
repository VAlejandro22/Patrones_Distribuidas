#PATRON OBSERVER
# Subject
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

# Observer Interface
class Observer:
    def update(self, temperature):
        pass

# Concrete Observer: Móvil
class MobileApp(Observer):
    def update(self, temperature):
        print(f"Notificación móvil: Temperatura actual: {temperature}°C")

# Concrete Observer: Pantalla
class DisplayScreen(Observer):
    def update(self, temperature):
        print(f"Pantalla: Temperatura actual: {temperature}°C")

# Uso OBSERVER
station = WeatherStation()
mobile_app = MobileApp()
screen = DisplayScreen()

station.add_observer(mobile_app)
station.add_observer(screen)

station.set_temperature(25)  # Notifica a ambos observadores
station.set_temperature(30)  # Notifica nuevamente