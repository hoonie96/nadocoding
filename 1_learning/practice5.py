### 6-1 if 분기(이런상황에서는 이런코드 저런상황에선느 저런코드)

# if 조건:
#     실행 명령문

weather = input("오늘 날씨는 어때요? ex)비,눈,미세먼지 ")  
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온이 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨예요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")


### 6-2 for 
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

#randrange()
for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


### 6-3 while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기처분되었습니다.")

customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회.".format(customer, index))
    index += 1 # 무한 루프
    break

customer = "토르"
person = "Unknown"

while person != customer: #조건에 만족할 때 까지 루핑
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")


### 6-4 continue 와 break 
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))


### 6-5 한 줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 전환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) 