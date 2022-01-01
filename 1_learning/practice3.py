### 4-1 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고
파이썬은 쉬워요
"""
print(sentence3) # """ 사용으로 4줄 전체가 들어감


### 4-2 슬라이싱
# 필요한것만 잘라서 쓰는걸 슬라이싱이라 한다
jumin = "960310-1077411"

print("성별 : " + jumin[7])
print("년 : " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # :사용 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # : 사용 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째 부터 정방향 끝까지


### 4-3 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # True
print(len(python)) # 문자 갯수 세기
print(python.replace("python", "Java")) # 대,소문자 상관없음

index = python.index("n") # 어떤 문자가 어느 위치에 있는지 찾기
print(index)
index = python.index("n", index + 5) # 해당된 문자의 +1의 위치가 어디인지 찾기 (얼마를 더하던 멕시멈에 위치한 값을 줌)
print(index)

print(python.find("Java")) # False retrun -1
#print(python.index("Java")) # error 해당 단어가 없어서 오류가 됌 그리고 다음 줄로 못 넘어감
print("hi")

print(python.count("n")) # 대,소문자 상관 없이 해당 단어가 몇번 반복 되는 수 세기


### 4-4 문자열 포맷
#print("a" + "b")
#print("a", "b")

# 방법 1
print("나는 %d살 입니다." % 20) # 정수 integer
print("나는 %s을 좋아해요." % "파이썬") # 문자열 string
print("Apple 은 %c로 시작해요." % "A") # 문자 char
# %s
print("나는 %s살 입니다." % 20) # 정수 integer
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간")) # 여러 항목이 있으면 괄호 처리

# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 중괄호를 쓸데 에는 연속적으로 입력한 값이 나옴
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 숫자를 넣으면 순번에 맞게 출력
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 숫자를 넣으면 순번에 맞게 출력

# 방법 3
print("나는 {age}살이며, {colour}색을 좋아해요.".format(age = 15, colour = "보라")) # 순번에 상관없이 정해진 값을 출력해줌

# 방법 4 (v3.6 이상~)
age = 10
colour = "파란"
print(f"나는 {age}살이며, {colour}색을 좋아해요.")


### 4-5 탈출문자
# \n : 줄바꿈
print("백문이 불여일건\n백견이 불여일타")

# 저는 "나도코딩" 입니다
print("저는 '나도코딩'입니다.") # 같은 따음표를 못씀
print('저는 "나도코딩"입니다.') # 큰, 작은 따음표로 구분 가능
print("저는 \"나도코딩\"입니다.") # \로 상관없이 사용 가능

# \\ : 문장 내에서 \
print("C:\\Users\\hooni\\Documents\\pythonworkspace>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # \r 뒤에 문자의 수 만큼 바꿈

# \b : 백스페이스 (한 글자 삭제)
print("Redd\b Apple")

# \t : 탭
print("Red\tApple")

