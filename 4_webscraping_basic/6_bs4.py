import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 우리가 가져온 html 문서를 lxml passer 를 통해서 BeautifulSoup 개체로 만듬
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element 의 속성 정보 dictionary 형태로 출력
print(soup.a["href"]) # a element 의 href 속성 '값' 정보를 출력
# 보통 위 문구들은 웹사이트에 대한 정보를 잘 알고 있을 때 사용. 

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a element 를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘
# 하나밖에 없어서 같은 결과. 어떤 tag 인지 명시해주면 더 정확하게 위치를 찾을 수 있음. 

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a) # rank1 안에 a element 만 출력

# print(rank1.a.get_text())
# print(rank1.next_sibling) # 아무것도 안나오면 어떤 개행(줄바꿈) 정보가 있을 수 있기 때문에 다시 한번 해주면 됌
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li") 
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li") 
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="먹는 인생-18화 고등어구이") # 해당 text 가 포함된 a 태그 가져오기
print(webtoon)