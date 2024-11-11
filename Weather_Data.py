import requests
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


##
##!!TASK C-1!!
##
#Create class for instance variables

class WeatherData:
    def __init__(self, latitude, longitude, month, day, year):
       # Variables for user input:
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year

       # Variables placeholders for calculations
        self.AVG_Temp = None
        self.MIN_Temp = None
        self.MAX_Temp = None
        self.AVG_Wind = None
        self.MIN_Wind = None
        self.MAX_Wind = None
        self.AVG_Precip = None
        self.MIN_Precip = None
        self.MAX_Precip = None


##
##!!TASK-C2!!
##

#Creating methods to pull data from weather api

    #Average Temperature method
    def get_avg_temp(self):
        temps = []
        for year in range(self.year - 5, self.year):
            date = f"{year}-{self.month:02d}-{self.day:02d}"
            parameters = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "start_date": date,
                "end_date": date,
                "temperature_unit": "fahrenheit",
                "timezone": "America/Chicago",
                "daily": "temperature_2m_max"
            }
            response = requests.get("https://archive-api.open-meteo.com/v1/archive", params=parameters)
            response.raise_for_status()
            data = response.json()
            if "daily" in data and "temperature_2m_max" in data["daily"]:
                temp = data['daily']['temperature_2m_max'][0]
                temps.append(temp)

        if temps:
            avg_temp = sum(temps) / len(temps)
            self.AVG_Temp = avg_temp
            self.MIN_Temp = min(temps)
            self.MAX_Temp = max(temps)
            return avg_temp
        else:
            print("No temperature data available for the specified period.")
            return None


    #Average wind speed method
    def get_avg_wind_speed(self):
        wind_speeds = []
        for year in range(self.year - 5, self.year):
            date = f"{year}-{self.month:02d}-{self.day:02d}"
            parameters = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "start_date": date,
                "end_date": date,
                "timezone": "America/Chicago",
                "daily": "windspeed_10m_max"
            }
            response = requests.get("https://archive-api.open-meteo.com/v1/archive", params=parameters)
            response.raise_for_status()
            data = response.json()
            if "daily" in data and "windspeed_10m_max" in data["daily"]:
                wind_speed = data['daily']['windspeed_10m_max'][0]
                wind_speeds.append(wind_speed)

        if wind_speeds:
            avg_wind = sum(wind_speeds) / len(wind_speeds)
            self.AVG_Wind = avg_wind
            self.MIN_Wind = min(wind_speeds)
            self.MAX_Wind = max(wind_speeds)
            return avg_wind
        else:
            print("No wind speed data available for the specified period.")
            return None


    #Average Wind Speed method
    def get_avg_precipitation(self):
        precipitations = []
        for year in range(self.year - 5, self.year):
            date = f"{year}-{self.month:02d}-{self.day:02d}"
            parameters = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "start_date": date,
                "end_date": date,
                "precipitation_unit": "inch",
                "timezone": "America/Chicago",
                "daily": "precipitation_sum"
            }
            response = requests.get("https://archive-api.open-meteo.com/v1/archive", params=parameters)
            response.raise_for_status()
            data = response.json()
            if "daily" in data and "precipitation_sum" in data["daily"]:
                precipitation = data['daily']['precipitation_sum'][0]
                precipitations.append(precipitation)

        if precipitations:
            avg_precip = sum(precipitations) / len(precipitations)
            self.AVG_Precip = avg_precip
            self.MIN_Precip = min(precipitations)
            self.MAX_Precip = max(precipitations)
            return avg_precip
        else:
            print("No precipitation data available for the specified period.")
            return None



##
##!!TASK C-4!!
##
#Set up the database for weather data

class WeatherRec(Base):
    __tablename__ = 'weather_records'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)
    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    avg_wind = Column(Float)
    min_wind = Column(Float)
    max_wind = Column(Float)
    avg_precip = Column(Float)
    min_precip = Column(Float)
    max_precip = Column(Float)

def setup_database():
    engine = create_engine('sqlite:///weather_data.db')
    Base.metadata.create_all(engine)
    return engine
