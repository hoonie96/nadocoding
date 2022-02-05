import os
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

os.chdir("C:/Users/hooni/Documents/coding/nadocoding/4_webscraping_basic")

filename = "12_시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # 자동 줄 바꿈 없애기 위해 newline 은 공백으로. excel 에서 열 때 encoding="utf-8-sig" 로 설정 utf8 은 텍스트 파일에서만 한글이 안 깨지게 함
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", "현재가", "전일비", "등락률", ...]
print(type(title))
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip
            continue  
        data = [column.get_text().strip() for column in columns] # 한 줄 for - [i for i in lst]. strip() 함수는 필요없는 글자 없애줌
        # print(data)
        writer.writerow(data)

# Reference
# strip()
# https://www.w3schools.com/python/ref_string_strip.asp
