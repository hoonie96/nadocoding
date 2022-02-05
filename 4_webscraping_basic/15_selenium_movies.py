# 동적 페이지 = 페이지가 접속 될때 불러와 지는게 아니고 사용자가 어떤 액션을 했을때 동작하는 페이지
# ex) 스크롤을 내렸을 때 새로운 목록을 게시 한다는지

import os
import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    # "Aceept-Language":"ko-KR,ko"
    }
# 사용자의 환경에 따라 언어 설정을 요함. 기본 영어로 설정되어 있음

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

os.chdir("C:/Users/hooni/Documents/coding/nadocoding/4_webscraping_basic")
# with open("15_movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)