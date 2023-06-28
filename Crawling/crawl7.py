from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
import time

# 크롬 드라이버 경로 설정
driver = webdriver.Chrome()

# csv 파일 생성
csv_file = open('player_stats.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

# 헤더 추가
csv_writer.writerow(['Player', 'AVG', 'OBP', 'SLG', 'OPS', 'ERA', 'WHIP', 'K/9'])

# 크롤링할 페이지 수
page_num = 10
player_stats_url = '<https://www.statiz.co.kr/player.php?opt=3&name=>'

for i in range(1, page_num + 1):
    # 페이지 이동
    driver.get(player_stats_url + str(i))

    # 페이지 로딩 대기
    time.sleep(2)

    # 페이지 소스코드 가져오기
    html = driver.page_source

    # BeautifulSoup 라이브러리를 이용해 HTML 코드에서 필요한 정보를 추출
    soup = BeautifulSoup(html, 'html.parser')
    players = soup.select('tbody > tr')

    for player in players:
        # 필요한 정보 추출
        player_name = player.select_one('a').text
        stats = player.select('td.statdata')

        # 필요한 정보를 csv 파일에 저장
        csv_writer.writerow([player_name, stats[0].text, stats[1].text, stats[2].text, stats[3].text, stats[4].text, stats[5].text, stats[6].text])

# csv 파일 닫기
csv_file.close()

# 크롬 드라이버 종료
driver.quit()