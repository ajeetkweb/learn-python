# test_weather.py
import unittest
from unittest.mock import patch
from weather import get_weather

class TestWeather(unittest.TestCase):
    
    @patch('weather.requests.get')
    def test_get_weather(self, mock_get):
        mock_get.return_value.json.return_value = {'temp': '22C'}

        result = get_weather("London")
      
        self.assertEqual(result['temp'], '22C')



if __name__ == "__main__":
    unittest.main()

