import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

# 요청이 성공했는지 확인
if response.status_code == 200:
    # HTML문서를 parsing
    soup = BeautifulSoup(response.text,
                         "html.parser")

    movies = soup.select("tbody.lister-list > tr")

    result = {}
    for movie in movies:
        title = movie.select_one("td.titleColumn > a").get_text().strip()
        rating = movie.select_one("td.ratingColumn > strong").get_text()
        result[title] = rating
    print(result)