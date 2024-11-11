import unittest
from Weather_Data import WeatherData, setup_database, WeatherRec
from main import session

class TestWeatherData(unittest.TestCase):
    def setUp(self):
        self.weather_data = WeatherData(latitude=38.5726, longitude=-90.8821, month=8, day=19, year=2025)

    def test_avg_temp_calculation(self):
        avg_temp = self.weather_data.get_avg_temp()
        self.assertIsNotNone(avg_temp, "Average temperature should not be None")
        self.assertIsInstance(avg_temp, float, "Average temperature should be a float")

    def test_avg_wind_speed_calculation(self):
        avg_wind = self.weather_data.get_avg_wind_speed()
        self.assertIsNotNone(avg_wind, "Average wind speed should not be None")
        self.assertIsInstance(avg_wind, float, "Average wind speed should be a float")

    def test_avg_precip_calculation(self):
        avg_precip = self.weather_data.get_avg_precipitation()
        self.assertIsNotNone(avg_precip, "Average precipitation should not be None")
        self.assertIsInstance(avg_precip, float, "Average precipitation should be a float")

if __name__ == '__main__':
    unittest.main()