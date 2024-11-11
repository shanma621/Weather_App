from Weather_Data import WeatherData, setup_database, WeatherRec
from sqlalchemy.orm import sessionmaker

# !!Task C-3!!
# Create a main.py file type and create an instance of the class in part C1 to call the methods used in part C2 for the daily weather variables.
# Create an instance of the SQLAlchemy session
engine = setup_database()
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    latitude = 38.5726
    longitude = -90.8821

    month = int(input("Enter the month number 1-12: "))
    day = int(input("Enter the day of the month 1-31: "))
    year = int(input("Enter the 4 digit year (ex 2024): "))

    date_weather = WeatherData(latitude, longitude, month, day, year)

    avg_temp = date_weather.get_avg_temp()
    if avg_temp is not None:
        print(f"Average temperature on {month:02d}-{day:02d} for the past 5 years: {avg_temp:.2f}°F")
    else:
        print("Average temperature data not available.")

    avg_wind = date_weather.get_avg_wind_speed()
    if avg_wind is not None:
        print(f"Average max wind speed on {month:02d}-{day:02d} for the past 5 years: {avg_wind:.2f} mph")
    else:
        print("Average wind speed data not available.")

    avg_precip = date_weather.get_avg_precip()
    if avg_precip is not None:
        print(f"Average total precipitation on {month:02d}-{day:02d} for the past 5 years: {avg_precip:.2f} inches")
    else:
        print("Average precipitation data not available.")

    date_weather.get_max_and_min_temp()
    if date_weather.MAX_Temp is not None and date_weather.MIN_Temp is not None:
        print(f"Max temperature on {month:02d}-{day:02d} for the past 5 years: {date_weather.MAX_Temp:.2f}°F")
        print(f"Min temperature on {month:02d}-{day:02d} for the past 5 years: {date_weather.MIN_Temp:.2f}°F")
    else:
        print("Max or min temperature data not available.")

    date_weather.get_max_and_min_wind()
    if date_weather.MAX_Wind is not None and date_weather.MIN_Wind is not None:
        print(f"Max wind speed on {month:02d}-{day:02d} for the past 5 years: {date_weather.MAX_Wind:.2f} mph")
        print(f"Min wind speed on {month:02d}-{day:02d} for the past 5 years: {date_weather.MIN_Wind:.2f} mph")
    else:
        print("Max or min wind speed data not available.")

    date_weather.get_max_and_min_precip()
    if date_weather.MAX_Precip is not None and date_weather.MIN_Precip is not None:
        print(f"Max precipitation on {month:02d}-{day:02d} for the past 5 years: {date_weather.MAX_Precip:.2f} inches")
        print(f"Min precipitation on {month:02d}-{day:02d} for the past 5 years: {date_weather.MIN_Precip:.2f} inches")
    else:
        print("Max or min precipitation data not available.")

    # Store the data in the database
    new_record = WeatherRec(
        latitude=latitude,
        longitude=longitude,
        month=month,
        day=day,
        year=year,
        avg_temp=avg_temp,
        min_temp=date_weather.MIN_Temp,
        max_temp=date_weather.MAX_Temp,
        avg_wind=avg_wind,
        min_wind=date_weather.MIN_Wind,
        max_wind=date_weather.MAX_Wind,
        avg_precip=avg_precip,
        min_precip=date_weather.MIN_Precip,
        max_precip=date_weather.MAX_Precip
    )

    session.add(new_record)
    session.commit()
    print("Data successfully added to the database.")

    # !!Task C-6 - Method to query and display data
    def query_weather_data(lat, long, m, d, y):
        records = session.query(WeatherRec).filter_by(latitude=lat, longitude=long, month=m, day=d, year=y).all()
        if records:
            print(f"\nWeather Data for {lat}, {long} on {m:02d}-{d:02d}-{y}\n")
            for record in records:
                print(f"""
                ID: {record.id}
                Latitude: {record.latitude}
                Longitude: {record.longitude}
                Date: {record.month:02d}-{record.day:02d}-{record.year}
                Average Temperature: {record.avg_temp:.2f}°F
                Min Temperature: {record.min_temp:.2f}°F
                Max Temperature: {record.max_temp:.2f}°F
                Average Wind Speed: {record.avg_wind:.2f} mph
                Min Wind Speed: {record.min_wind:.2f} mph
                Max Wind Speed: {record.max_wind:.2f} mph
                Average Precipitation: {record.avg_precip:.2f} inches
                Min Precipitation: {record.min_precip:.2f} inches
                Max Precipitation: {record.max_precip:.2f} inches
                """)
        else:
            print("No data found for the specified date and location.")

    query_weather_data(latitude, longitude, month, day, year)
