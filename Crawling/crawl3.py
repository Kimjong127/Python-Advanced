import requests
from bs4 import BeautifulSoup

url = "http://www.weather.com"

response = requests.get(url)

# 요청이 성공했는지 확인
if response.status_code == 200:
    # HTML문서를 parsing
    soup = BeautifulSoup(response.text,
                         "html.parser")

    weathers = soup.find_all("div", class_="ListItem--listItem--25ojW WeatherDetailsListItem--WeatherDetailsListItem--1CnRC")

    result = {}
    for weather in weathers:
        key_name = weather.find("div", class_="WeatherDetailsListItem--label--2ZacS").get_text()
        value = weather.find("div", class_="WeatherDetailsListItem--wxData--kK35q").get_text()
        result[key_name] = value
    print(result)