import unittest


from world_weather import (
    format_date_long,
    format_date_short,
    mtr_per_sec_to_km_per_hour,
)
#jsonschema validation
def test_weather_data_validation():
    api_key = "your_test_api_key"
    city = "Test City"
    data = get_weather_data(api_key, city)
    assert data is not None, "API response did not validate against the schema"

class WorldWeatherTest(unittest.TestCase):
    def test_speed(self):
        self.assertEqual(10.8, mtr_per_sec_to_km_per_hour(3))

    def test_format_date(self):
        iso = "2023-05-24"
        self.assertEqual("24 May", format_date_short(iso))
        self.assertEqual("Wed, 24 May", format_date_long(iso))


    #Edge case testing 
    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            format_date_long("24-05-2023")
        with self.assertRaises(ValueError):
            format_date_short("05-24-2023")

    def test_negative_speed(self):
        self.assertEqual(-10.8, mtr_per_sec_to_km_per_hour(-3))

    def test_zero_speed(self):
        self.assertEqual(0, mtr_per_sec_to_km_per_hour(0))


    #boundry testing 
    def test_end_of_year_date_format(self):
        self.assertEqual("31 Dec", format_date_short("2023-12-31"))
        self.assertEqual("Sun, 31 Dec", format_date_long("2023-12-31"))

    def test_beginning_of_year_date_format(self):
        self.assertEqual("01 Jan", format_date_short("2024-01-01"))
        self.assertEqual("Mon, 01 Jan", format_date_long("2024-01-01"))


    #Integration Testing
    def test_get_current_weather_integration(self):
        from unittest.mock import patch
        mock_data = {
            "data": [{"city_name": "Test City", "country_code": "TC", "temp": 20, "weather": {"code": 200, "description": "Sunny"}}]
        }
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.json.return_value = mock_data
            weather = get_current_weather("fake_api_key", "Test City")
            self.assertEqual(weather, mock_data)
    
    #performance testing 
    def test_performance_speed_conversion(self):
        import time
        start_time = time.time()
        for i in range(100000):
            mtr_per_sec_to_km_per_hour(10)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1)

