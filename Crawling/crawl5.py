# Selenium 실습 (로그인하기)
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

url = "https://www.naver.com/"

driver = webdriver.Chrome()   # Selenium 사용시 드라이버 생성

# 페이지 접근
driver.get(url)

# 페이지 정지(설정을 해놓지 않으면 켜지고 바로 꺼진다.)
time.sleep(1)

# 로그인창 클릭
driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()
time.sleep(2)

# 네이버 id, pw
naver_id = 'kkimjh127'
naver_pw = 'tlqkfsus8989!'

# ID 입력하기 (봇감지 프로그램 우회하기->클립보드에 복사후 붙여넣는 방식)
# driver.find_element(By.ID, 'id').send_keys(naver_id)
id_input = driver.find_element(By.ID, 'id')    # ID를 변수에 대입
pyperclip.copy(naver_id)                       # ID복사(ctrl + c)      
id_input.click()                               # ID창 클릭
id_input.send_keys(Keys.CONTROL, 'v')          # ID붙여넣기(ctrl + v)
time.sleep(2)

# Password 입력하기
# driver.find_element(By.ID, 'pw').send_keys(naver_pw)
pw_input = driver.find_element(By.ID, 'pw')
pyperclip.copy(naver_pw)
pw_input.click()
pw_input.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 로그인버튼 클릭
# driver.find_element(By.CLASS_NAME, "btn_login").click()
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
time.sleep(10)
