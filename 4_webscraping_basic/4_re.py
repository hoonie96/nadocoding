# re = regular expression (정규식 = 정해진 형태를 의미하는 식)

# 주민등록번호 (6 자리 숫자, - 추가, 7 자리 숫자 순) 
# 123456-1234567                O
# abcdef-1111111                X

# 이메일 주소 (문자, @ 추가, 문자, . 추가, 문자 순)
# nadocoding@gmail.com          O
# nudocoding@gmail@gmail.com    X

# 차량 번호 (2~3 자리 숫자, 문자 1개, 4 자리 숫자 순)
# 11가 1234                     O
# 123가 1234                    O

# IP 주소 (0~255 사이의 숫자의 묶음, 사이마다 . 추가)
# 192.168.1.1                   O
# 1000.2000.3000.4000           x


import re
# 차 번호판이 4 자리 문자로 구성
# 예시 : abcd, book, desk
# 차 번호 판 : ca?e
# 완성 단어 유추로 맞추기 : care, cafe, case, cave
# 알파벳 순서로 맞추기 : caae, cabe, cace, cade, ...

p = re.compile("ca.e") # p(패턴)은 어떤 정규식을 컴파일 할지 정해주는 것
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작 > desk, destination (O) |fade (X)
# $ (se$)  : 문자열의 끝 > case, base (O) | face (X)

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작 > desk, destination (O) |fade (X)
# $ (se$)  : 문자열의 끝 > case, base (O) | face (X)

# Reference : Python re(Regular Expression)
# https://www.w3schools.com/python/python_regex.asp
# https://docs.python.org/3/library/re.html