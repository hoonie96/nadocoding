# Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

# [조회 조건]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]
# ========== 매물 1 ==========
# 거래 : 매매
# 면적 : 84/59
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
# ========== 매물 2 ==========
#     ...

# [주의 사항]
# - 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능

######################################################

# 1. https://new.land.naver.com/complexes 네이버 부동산 매물 접속
# 2. '제주 외도1동 부영2차
# 3. 전체 거래 결과 정보 조회 및 출력

import os
import requests
from bs4 import BeautifulSoup

url = "https://new.land.naver.com/complexes/104524?ms=33.48681,126.433479,17&a=APT:ABYG:JGC&e=RETAIL"
# url = "https://new.land.naver.com/complexes"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

os.chdir("C:/Users/hooni/Documents/coding/nadocoding/4_webscraping_basic")
with open("19_quiz_request.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

# for movie in movies:
#     title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
#     print(title)