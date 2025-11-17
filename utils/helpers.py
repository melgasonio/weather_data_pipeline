# Tranform a weather api response into a dict with specific keys
def transform_weather_response(response, timestamp, name):
        transformed_data = {}

        transformed_data["timestamp"] = timestamp
        transformed_data["city"] = name
        transformed_data["weather"] = response["weather"][0]["description"]
        
        transformed_data["temp"] = response["main"]["temp"]
        transformed_data["temp"] = convert_to_celsius(transformed_data["temp"])
        
        transformed_data["temp_min"] = response["main"]["temp_min"]
        transformed_data["temp_min"] = convert_to_celsius(transformed_data["temp_min"])
        
        transformed_data["temp_max"] = response["main"]["temp_max"]
        transformed_data["temp_max"] = convert_to_celsius(transformed_data["temp_max"])
        
        transformed_data["humidity"] = response["main"]["humidity"]

        return transformed_data
    
# Convert Kelvin temperature to Celsius
def convert_to_celsius(kelvin):
    return kelvin - 273.15