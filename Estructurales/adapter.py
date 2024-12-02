class ExternalWeatherAPI:
    def fetch_temperature_in_celsius(self):
        return 25.5  # Supongamos que esto viene de la API.

class WeatherAdapter:
    def __init__(self, api):
        self.api = api

    def get_temperature(self):
        return self.api.fetch_temperature_in_celsius()
    
# Uso ADAPTER
external_api = ExternalWeatherAPI()
weather_adapter = WeatherAdapter(external_api)

print(f"La temperatura es: {weather_adapter.get_temperature()}°C")