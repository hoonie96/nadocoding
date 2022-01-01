# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분을 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규치3 : 남은 글자 중에 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!' 로 구성
#                 (nav)                (5)                (1)         (!)
# 예) 생성된 비밀번호 : nav51!

# 내 방법
# url = input("예) http://naver.com\n웹사이트를 입력하세요: ")
# print("생성된 비밀번호 : " + url[7:10] + str(len(url[7:]) - 4) + str(url.count('e')) + "!")
# 문제점 : url.count("e")에서 url전체중에 "e"를 찾기때문에 "".net"에서 "e"발견 되는 문제 있음

# 답안
url = "http://google.com" # 주소만 바꾸고 답 확인하기
my_str = url.replace("http://", "") # 규칙 1
# print(my_str) # 중간 점검
my_str = my_str[:my_str.index(".")]
# my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4) 처음부터 점(.)의 위치 까지
# print(my_str) # 중간 점검
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))