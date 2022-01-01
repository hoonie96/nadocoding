# 7-1 표준입출력
# print("Python", "Java", "JavaScript", sep=" vs ") 띄어쓰기 대신 sep에 입력된 내용이 대신해서 구분해줌
# print("Python", "Java", "JavaScript", sep=",", end="?") #end 가 붙으면서 ?로 끝나게 만들어 줄 바꿈이 아닌 두 print를 하나로 묶어서 출력됨
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) #표준 출력
# print("Python", "Java", file=sys.stderr) #표준 에러

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():  # 순차적으로 scores안에 있는 items인 subject, score들이 자동적으로 variable로 저장됨
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")  # 사용자 입력을 통해서 값을 받게 되면 항상 문자열(str)로 받게됨 
# print(type(answer)) = class 'str'
# answer = 10
# print(type(answer)) = class 'int'
# # print("입력하신 값은 " + answer + "입니다.")


# 7-2 다양한 출력포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500)) # 빈공간을 스페이스로 넣고 오른쪽 정렬 후에 500 출력
# 7자리의 여백과 500이 오른쪽애 출력 됨으로 총 10자리 공간을 사용

# 부호 추가 후 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500)) # 따로 + 없이도 +출력
# print("{0: >+10}".format(-500))

# 왼쪽 정렬 후 빈칸을 _로 채움
# print("{0:_<+10}".format(500))

# 3자리 마다 ,찍어주기 - 자동적으로 3자리 마다 찍힘
# print("{0:,}".format(100000000000))
# print("{0:+,}".format(-100000000000)) 
# 3자리 마다 ,찍어주기, 부호도 붙이고 자릿수 확보하기
# print("{0:^<+30,}".format(-100000000000)) # 오른순으로 진행 ,를 3자리마다 찍고 30자리 확보하고 부호 넣고 왼쪽 정렬하고 빈칸에 ^출력 하고

#소수점 출력
# print("{0:f}".format(5/3))
#소수점 특정 자리까지만 출력 (소수점 3째 자리에서 반올림, 2자리까지만 출력)
# print("{0:.2f}".format(5/3))


# 7-3 파일 입출력
# 입력하기
# score_file = open("score.txt", "w", encoding="utf8") #파일 이름, w: 쓰기, encoding 정보: 정의를 안해주면 한글이 깨지는 경우가 있음
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #파일 이름, a: 첨부, encoding 정보: 정의를 안해주면 한글이 깨지는 경우가 있음
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 출력하기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) # 파일에 있는 모든 내용 출력
# score_file.close()

# 1
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄 변경을 안하고 싶다면 끝을 빈공간으로 출력
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 2
# score_file = open("score.txt", "r", encoding="utf8")
# while True: # 무한 루프
#     line = score_file.readline() # 한 줄 씩 읽기
#     if not line: # 읽어 올 라인이 없으면
#         break # 반복문 탈출
#     print(line, end="") 
# score_file.close()

# 3
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines: # list 에 있는 line 한 줄 씩 불러와서 출력
#     print(line, end="")
# score_file.close()


# 7-4 pickle
# 프로그램 상에서 사용하고 있는 데이터를 파일형태로 저장 해주는거
import pickle
profile_file = open("profile.pickle", "wb") # pickle 을 이용할 땐 항상 b(binary) 입력해야함
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]} # dictionary
print(profile)
pickle.dump(profile, profile_file) # dump 를 이용해 profile 에 있는 정보를 profile_file 에 저장
profile_file.close()

# 파일 안에 있는 데이터 가져오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # load 를 이용해 profile_file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

# 7-5 with
# 읽어 오고 출력
import pickle
with open("profile.pickle", "rb") as profile_file: # rb 로 profile.pickle 을 열고 profile_file 이라는 변수에 저장
    print(pickle.load(profile_file)) # 그리고 pickle.load 를 통해서 profile_file 을 읽어 올수 있음
# 따로 profile_file.close() 를 통해 닫아줄 필요 가 없음 with 를 통해 자동으로 닫힘

# 파일을 만들어 내용 적기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

