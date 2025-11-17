from dotenv import load_dotenv
import os
from datetime import datetime

from utils.openweathermap_api import OpenWeatherMap
from utils.pandas import convert_to_df
from utils.helpers import transform_weather_response

'''
Construct live weather data of Baguio City, PH and Tokyo, Japan as a dataframe
Final dataframe only contains temperature and humidity information
'''
def main():
    # Pull live weather data and leave a timestamp footprint
    load_dotenv()
    key = os.getenv("API_KEY")
    now = datetime.now().isoformat()
    
    locations = [{"city": "Baguio City", "country_code": "PH"}, {"city": "Tokyo","country_code": "JP"}]
    responses= []
    
    api = OpenWeatherMap(key)
    
    for location in locations:
        name = location["city"]
        transformed_data = {}
        weather_data = api.get_weather_data(location["city"], location["country_code"])

        # Return a new dict based on original response data where some keys are removed and kept, and temperature data are converted into Celsius
        transformed_data = transform_weather_response(weather_data, now, name)
        responses.append(transformed_data)
    
    df = convert_to_df(responses)
    print(df)
    
if __name__ == "__main__":
    main()