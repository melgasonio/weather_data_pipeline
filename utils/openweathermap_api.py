import requests

class OpenWeatherMap():
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_lat_long(self, city):
        key = self.api_key
        country_code = "PH"
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&appid={key}"
        
        response = requests.get(url)
        data = response.json()
        
        return data
        