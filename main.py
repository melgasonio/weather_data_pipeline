from dotenv import load_dotenv
import os
from datetime import datetime

from utils.openweathermap_api import OpenWeatherMap
from utils.pandas import convert_to_df, delete_col, add_col
from utils.helpers import get_keys_as_list, remove_arr_elems

'''
Construct live weather data of Baguio City, PH and Tokyo, Japan as a dataframe
Final dataframe only contains temperature and humidity information
'''
def main():
    # Pull live weather data and leave a timestamp footprint
    load_dotenv()
    key = os.getenv("API_KEY")
    now = datetime.now()

    locations = [{"city": "Baguio City", "country_code": "PH"}, {"city": "Tokyo","country_code": "JP"}]
    responses= []
    
    api = OpenWeatherMap(key)
    
    for location in locations:
        weather_data = api.get_weather_data(location["city"], location["country_code"])
        responses.append(weather_data)
        
    # Manipulate the weather data as a dataframe  
    df = convert_to_df(responses)
    df = add_col(df, "timestamp", [now] * len(locations))
    
    # Update dataframe's columns and drop irrelevant ones
    response_sample = responses[0]
    response_keys = get_keys_as_list(response_sample)
    df_new_columns = ["weather", "main", "name"]
    response_keys = remove_arr_elems(response_keys, df_new_columns) # Drop these columns
    df = delete_col(df, response_keys)
    
    print(df)
    
if __name__ == "__main__":
    main()