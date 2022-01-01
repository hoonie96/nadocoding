### 7-1 함수(function)

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


### 7-2 전달값과 반환값
def deposit(balance, money): # 입금
    print("입급이 완료 되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원 입니다".format(balance - money))
        return balance - money
    else: # 잔액이 출금보다 적으면
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance, 500)
#balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다".format(commission, balance))


# 7-3 기본값
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업 일때.

def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")


# 7-4 키워드값 (순서가 뒤섞여 있어도 함수 호출.)
def profiles(name, age, main_lang):
    print("키워드값:", name, age, main_lang)  

profiles(name="유재석", main_lang="파이썬", age=20)
profiles(main_lang="자바", age=25, name="김태호")


# 7-5 가변인자
# def profile1(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile1("유재석", 20, "Python", "Java", "C", "C++", "C#") # 언어가 더 많을때?
# profile1("김태호", 25, "Kotlin", "Swift", "", "", "") # 언어가 적을때?
# # 매번 fucntion을 고쳐줘야 함. 그래서 가변인자를 이용

def profile1(name, age, *language): # 가변인자 *
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="a")
    for lang in language:
        print(lang, end=" ") # lang 가 끝날 때 마다 end 를 적용
    print()

profile1("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript") # 언어가 더 많을때?
profile1("김태호", 25, "Kotlin", "Swift") # 언어가 적을때?

# 7-6 지역변수 전역변수 (local and global variable)
gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감 # 이것은 gun 을 global 로 function 안에 넣어서 결과를 출력
gun = checkpoint_ret(gun, 2) # 이것은 외부 gun 이라는 variable 를 function 안으로 호출 해서 계산된 값을 다시 외부 gun 에 대입
print("남은 총 : {0}".format(gun))