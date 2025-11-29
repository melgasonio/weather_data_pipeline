import math
import pandas as pd

# Tranform a weather api response into a dict with specific keys
def transform_weather_response(response, timestamp, name):
        transformed_data = {}

        transformed_data["timestamp"] = timestamp
        transformed_data["city"] = name
        transformed_data["weather"] = response["weather"][0]["description"]
        transformed_data["icon_id"] = response["weather"][0]["icon"]
        
        transformed_data["temp"] = response["main"]["temp"]
        transformed_data["temp"] = convert_to_celsius(transformed_data["temp"])
        
        transformed_data["temp_min"] = response["main"]["temp_min"]
        transformed_data["temp_min"] = convert_to_celsius(transformed_data["temp_min"])
        
        transformed_data["temp_max"] = response["main"]["temp_max"]
        transformed_data["temp_max"] = convert_to_celsius(transformed_data["temp_max"])
        
        transformed_data["humidity"] = response["main"]["humidity"]
        
        transformed_data["wind_speed"] = response["wind"]["speed"]
        transformed_data["wind_speed"] = convert_to_kmh(transformed_data["wind_speed"])

        return transformed_data
    
# Convert Kelvin temperature to Celsius
def convert_to_celsius(kelvin):
        return math.floor(kelvin - 273.15)

# Convert wind speed to km/h from m/s
def convert_to_kmh(windspeed):
        return math.floor(windspeed * 3.6)

# Create a row in the database table based on the dataframe row
def query_add_row(table, row):
        query = f"""
                INSERT INTO {table} (created_at, city, weather, icon_id, temperature,  temperature_min, temperature_max, humidity, wind_speed)
                VALUES (
                        '{row['timestamp']}',
                        '{row['city']}',
                        '{row['weather']}',
                        '{row['icon_id']}',
                        {row['temp']},
                        {row['temp_min']},
                        {row['temp_max']},
                        {row['humidity']},
                        {row['wind_speed']}                  
                )
        """
        return query

# Delete top two results after adding two new records
def query_delete_top(table):
        query = f"""
                WITH dispose as (
                        SELECT id
                        FROM {table}
                        ORDER BY id
                        LIMIT 2
                )
                DELETE FROM {table}
                WHERE id in (SELECT id FROM dispose);                
        """
        return query

# Convert an array of dictionaries to a dataframe
def convert_to_df(arr):
    return pd.DataFrame(arr)