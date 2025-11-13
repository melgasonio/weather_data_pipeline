import requests

class OpenWeatherMap():
    def __init__(self, api_key):
        self.api_key = api_key

        
    def get_weather_data(self, city):
        key = self.api_key

        fetch_lat_lon = self._get_lat_lon(city, key)
        data_object = fetch_lat_lon[0]
        lat = data_object["lat"]
        lon = data_object["lon"]
        
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
        
        response = requests.get(url)
        data = response.json()
        
        return data
        
    
    def _get_lat_lon(self, city, key):
        country_code = "PH"
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&appid={key}"
        
        response = requests.get(url)
        data = response.json()
        
        return data
        