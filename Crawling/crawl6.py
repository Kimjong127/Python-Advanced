# Selenium으로 이미지 파일 크롤링해오기

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
import time
import io, base64
import requests
from PIL import Image


# base64데이터 -> JPG
def base64ToJpg(base64_str, filename):
    image_data = base64_str.split(',')[1]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    # 이미지 저장
    image.save(filename, "JPEG") 

# url데이터 -> JPG
def urlToJpg(url, filename):
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    # 이미지 저장
    image.save(filename, 'JPEG')

## 시작
url = 'https://www.google.co.kr/imghp?hl=ko&ogbl'

driver = webdriver.Chrome()   # Selenium 사용시 드라이버 생성

# 페이지 접근
driver.get(url)

# 페이지 정지(설정을 해놓지 않으면 켜지고 바로 꺼진다.)
time.sleep(1)

query = "강아지"

# 검색창에 "고양이 입력"
driver.find_element(By.CLASS_NAME, "gLFyf").send_keys(query)
time.sleep(2)

# 검색창에 엔터
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button').send_keys(Keys.ENTER)
time.sleep(2)

# 마지막 이미지 처리 인덱스
last_index = 0
image_index = 0
last_height = driver.execute_script('return document.body.scrollHeight')
new_height = 0

while True:
    # 이미지 모두 가져오기
    all_images = driver.find_elements(By.CLASS_NAME, 'rg_i')
    images = all_images[last_index:]
    last_index = len(all_images)

    # 각 이미지 src속성 출력("http" or "base64" 두 종류)
    for image in images:
        src_path = image.get_attribute('src')
        
        if src_path is None:    # None값을 가지는 데이터 pass!
            continue

        filename = f"{query}-{image_index}"

        if src_path.startswith("https"):
            try:
                urlToJpg(src_path, f"images/{filename}.jpg")
                print(f"URL 이미지가 저장:{filename}")
            except:
                print("URL 이미지 저장 중 오류")
        elif src_path.startswith('data:image/jpeg;base64'):
            try:
                base64ToJpg(src_path, f"images/{filename}.jpg")
                print(f"base64 이미지가 저장:{filename}")
            except:
                print("base64 이미지 저장 중 오류")

        image_index += 1

    # 아래로 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height - last_height > 0:
        last_height = new_height
    else:
        try:
            more_btn = driver.find_element(By.CLASS_NAME, 'mye4qd')
            more_btn.click()
        except ElementNotInteractableException:
            break
