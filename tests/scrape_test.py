import unittest
from bs4 import BeautifulSoup
from src.scraper import get_google_weather, extract_text, parse_weather_info


class TestWebScraping(unittest.TestCase):
    def test_get_google_weather(self):
        response = get_google_weather()
        self.assertIsNotNone(response)

    def test_weather_div(self):
        html = get_google_weather("bangkok").text
        soup = BeautifulSoup(html, "html.parser")
        weather_div = soup.find("div", class_="Gx5Zad")
        print(weather_div)
        self.assertIsNotNone(weather_div)

    def test_extract_text(self):
        response = get_google_weather("bangkok")
        text = extract_text(response)
        self.assertNotEqual(len(text), 0)
        self.assertIn("กรุงเทพมหานคร", text)

    def test_parse_weather_info(self):
        response = get_google_weather("bangkok")
        text = extract_text(response)
        mock_data = [
            "กรุงเทพมหานคร",
            " / ",
            "สภาพอากาศ",
            "33°C",
            "33°C",
            "วันศุกร์ 14:13\nมีเมฆบางส่วน",
            "วันศุกร์ 14:13\nมีเมฆบางส่วน",
        ]
        expected_parsed_weather = {
            "city": "กรุงเทพมหานคร",
            "temp": "33°C",
            "day": "วันศุกร์",
            "time": "14:13",
            "weather": "มีเมฆบางส่วน",
        }
        parsed_weather = parse_weather_info(mock_data)
        self.assertEqual(parsed_weather, expected_parsed_weather)


if __name__ == "__main__":
    unittest.main()
