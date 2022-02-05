# HTTP protocol 을 통해서 서버에 요청을 보내면 서버는 그 요청에 맞게 응답을 해주는데 요청에 포함되는 것 중에 HTTP method 라는 것이 있음.
# 여기에는 몇 가지가 있는데 보편적으로 많이 사용 하는 get, post 방식
# get : 어떤 내용을 누구나 볼 수 있게 url 에 적어서 보내는 방식. 한번 전송할 때 보낼 수 있는 데이터 양이 제한되어 있음 
# https://www.coupang.com/np/search?minPrice=1000&maxPrice=100000&page=1
# ? 뒤에 있는 것들로 부터 변수와 값  
# post : HTTP Message Body 에 숨겨서 보내는 방식. 보안 데이터를 보낼 때 사용. 제한이 없기 때문에 큰 데이터나 파일 업로드 같은 걸 보낼 수 있음
# https://www.coupang.com/np/search?id=nadocoing&pw=1234
# 위와 같으면 보안이 낮아서 위험에 노출 될 가능성이 큼

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(res.text)

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("     <광고 상품 제외합니다>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    
    # 애플 제품 제외
    if "Apple" in name:
        print("     <Apple 상품 제외합니다>")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

    #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        # rate = "평점 없음"
        print("     <평점 없는 상품 제외합니다>")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text() # 출력 예: (26)
        rate_cnt = rate_cnt[1:-1] # 1 번째 인덱스 부터 -1 인덱스 까지만
        print("리뷰 수", rate_cnt)
    else:
        # rate_cnt = "평점 수 없음"
        print("     <평점 수 없는 상품 제외합니다>")
        continue
    
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, "/", price, "원 /", rate, "/", rate_cnt)
