# Selenium
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.naver.com/"

driver = webdriver.Chrome()   # Selenium 사용시 드라이버 생성

# 페이지 접근
driver.get(url)

# 페이지 정지(설정을 해놓지 않으면 켜지고 바로 꺼진다.)
time.sleep(1)

# 검색어 창에 자동으로 '인공지능' text 입력하기(find_element-하나만 찾기, find_elements-여러개 찾기:리스트로 반환)
# 검색창 element : <input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element="">
# driver.find_element(By.ID, "query").send_keys("인공지능")
# driver.find_element(By.CLASS_NAME, "search_input").send_keys("한국")
# driver.find_element(By.CSS_SELECTOR, '[placeholder="검색어를 입력해 주세요."]').send_keys("미국")
driver.find_element(By.XPATH, '//*[@id="query"]').send_keys('인공지능')
time.sleep(2)

# 검색버튼 클릭하기 
# 검색버튼 element : <button type="submit" class="btn_search" onclick="window.nclk_v2(this,&quot;sch.action&quot;)"> <span id="search-btn" class="ico_btn_search"></span> <span class="blind">검색</span> </button>
# driver.find_element(By.CLASS_NAME, 'btn_search').click()

# 검색창에 입력 후 엔터
driver.find_element(By.XPATH, '//*[@id="query"]').send_keys(Keys.ENTER)
time.sleep(2)

# 뉴스 탭 클릭하기
driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[4]/a').click()
time.sleep(2)

# 페이지 긁어오기(동일한 작업이므로 함수로 만들기)
def get_page_news_title():
    # 뉴스 제목 crawling하기 (HTML 코드 가져오기)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 뉴스 타이틀 리스트 찾기
    # <a href="http://www.newsis.com/view/?id=NISX20230613_0002336220&amp;cID=10802&amp;pID=14000" class="news_tit" target="_blank" onclick="return goOtherCR(this, 'a=nws*a.tit&amp;r=1&amp;i=88000127_000000000000000011909352&amp;g=003.0011909352&amp;u='+urlencode(this.href));" title="인천시, 초거대 인공지능과 지역특화산업 연계 모색">인천시, 초거대 <mark>인공지능</mark>과 지역특화산업 연계 모색</a>
    # <a href="https://www.yna.co.kr/view/AKR20230612058200003?input=1195m" class="news_tit" target="_blank" onclick="return goOtherCR(this, 'a=nws*a.tit&amp;r=6&amp;i=880000D8_000000000000000013995919&amp;g=001.0013995919&amp;u='+urlencode(this.href));" title="포스코이앤씨, 건설업계 최초 'AI+' 인공지능 인증 획득">포스코이앤씨, 건설업계 최초 'AI+' <mark>인공지능</mark> 인증 획득</a>
    news = soup.find_all('li', class_="bx")
    for n in news:
        title = n.find('a', class_='news_tit')
        if title is not None:
            result = title.get_text()
            print(result)

# 다음 페이지 이동(함수 생성)
def click_next_btn():
    # <a href="?where=news&amp;sm=tab_pge&amp;query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&amp;sort=0&amp;photo=0&amp;field=0&amp;pd=0&amp;ds=&amp;de=&amp;cluster_rank=23&amp;mynews=0&amp;office_type=0&amp;office_section_code=0&amp;news_office_checked=&amp;nso=so:r,p:all,a:all&amp;start=11" role="button" class="btn_next" aria-disabled="false" onclick="return goOtherCR(this, 'a=nws.paging&amp;r=2&amp;u='+urlencode(urlexpand(this.href)));"><i class="spnew ico_page_arr">다음</i></a>
    driver.find_element(By.CLASS_NAME, "btn_next").click()
    time.sleep(2)

# 10번 반복하기
for i in range(10):
    get_page_news_title()
    click_next_btn()