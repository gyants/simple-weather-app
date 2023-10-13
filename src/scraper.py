from bs4 import BeautifulSoup
import requests


def get_google_weather(weather=""):
    url = f"https://www.google.com/search?q=weather {weather}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response


def extract_text(response):
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    weather_div = soup.find("div", class_="Gx5Zad")  # class for weather card
    text_class = soup.find_all(class_="BNeawe")
    text = [i.get_text() for i in text_class]
    return text


def parse_weather_info(text_list):
    text = text_list[:6]
    city, temp = text[0], text[3]
    day, time = text[5].split(" ")
    time, weather = time.split("\n")
    data = {"city": city, "temp": temp, "day": day, "time": time, "weather": weather}
    return data
