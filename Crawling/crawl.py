import requests
from bs4 import BeautifulSoup

# pip install requests
# pip install beautifulsoup4

url = "http://quotes.toscrape.com/"

response = requests.get(url)

# 요청이 성공했는지 확인
if response.status_code == 200:
    # HTML문서를 parsing
    soup = BeautifulSoup(response.text,
                         "html.parser")

    quotes = soup.find_all("div", class_="quote")

    result = {}
    for quote in quotes:
        text = quote.find("span", class_='text').get_text()
        r_text = text[1:-2]
        author = quote.find('small', class_='author').get_text()
        result[author] = r_text
    print(result)
                        


