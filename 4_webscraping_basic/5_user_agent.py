import os
import requests

url = "http://nadocoding.tistory.com"
# 접속하는 brower 에 따라 user agent 가 달라질 수 있음. 그러므로 서버 입장에서는 UA(또는 의도)에 따라 정보를 조금 다르게 변환 할 수 있음
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

os.chdir("C:/Users/hooni/Documents/coding/nadocoding/4_webscraping_basic")

with open("5_nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)