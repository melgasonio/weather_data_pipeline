from dotenv import load_dotenv
import os
from datetime import datetime, timezone

from utils.openweathermap_api import OpenWeatherMap
from utils.db_server import DBServer
from utils.pandas import convert_to_df
from utils.helpers import transform_weather_response, query_add_row, query_delete_top

# AWS Lambda handler
def lambda_handler(event, context):
    main()
    return {"status": "success"}

'''
Construct live weather data of Baguio City, PH and Tokyo, Japan as a dataframe
Final dataframe only contains temperature and humidity information
'''
def main():
    # Pull live weather data and leave a timestamp footprint
    load_dotenv()
    key = os.getenv("API_KEY")   
    now = datetime.now(timezone.utc).isoformat()
    
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

    uri = os.getenv("DB_URI")
    table = os.getenv("DB_TABLE1")
    db = DBServer(uri)
    db.connect()
    # Map df dataframe correctly and add as a row to the database table
    for _, row in df.iterrows():
        query = query_add_row(table, row)
        db.execute_sql(query)
    # Delete top two rows immediately
    query = query_delete_top(table)
    db.execute_sql(query)
    db.close()
    
if __name__ == "__main__":
    main()