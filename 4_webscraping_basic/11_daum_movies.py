import os
import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images): # 똑같이 loop 가 도는데 0, 1, 2, 순으로 돔
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        print(image["src"])
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        os.chdir("C:/Users/hooni/Documents/coding/nadocoding/4_webscraping_basic/11_movie_images")

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f: #  idx 가 1~5 로 인해 년도가 바뀌면서 덮어 씌우기를 막기위해 year 변수를 넣어서 겹쳐지기 않게 보이게 함. ex) movie2.jpg -> movie_2015_1.jpg
            f.write(image_res.content)

        if idx >= 4: # 상위 5개 이미지까지만 다운로드
            break