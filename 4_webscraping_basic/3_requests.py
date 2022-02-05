import os
import requests

res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com") # 403 이 나왔어야 함
res.raise_for_status()
# 응답코드 : 403
# error~~~~~
# 밑이랑 같은 뜻이라 이렇게 쌍으로 쓴다

# print("응답코드 :", res.status_code) # 200 이면 정상

# if res.status_code == requests.codes.ok: # 200 이랑 같은 말
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print("웹 스크래핑을 진행합니다")
print(len(res.text))
print(res.text)

os.chdir("C:/Users/hooni/Documents/coding/nadocoding/4_webscraping_basic")

with open("3_mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)