import imp
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# running error 실행하자마자 바로 에러 발생 해결방법
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# browser = webdriver.Chrome(options=options)

# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url) # url 로 이동

time.sleep(1)

# 가는 날 선택 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
# browser.find_element_by_link_text("가는 날").click()

time.sleep(5)

# 이번달 27일, 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

time.sleep(5)

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 유용하게 사용 가능
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")) # WebDriverWait 를 통해서 browser 를 10초(최대값) 까지  xpath 기준으로 위에 명시된 값의 elements 가 나올때 까지 기다리게 함. 나오지 않을 시엔 EC 에러 반환
    # 성공했을 때 동작 수행
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem)