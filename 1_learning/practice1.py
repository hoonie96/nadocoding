### 2-1 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))


### 2-2 문자열 자료형
print('풍선')
print("나비")
print('ㅋㅋㅋㅋㅋㅋㅋ')
print('ㅋ'*7)


### 2-3 boolean 자료형
# 참 / 거짓 Ture / False
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not False)
print(not (5 < 10))


### 2-4 변수
# 애완동물을 소개해 주세요~
animal =  "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult_ = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요.")
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
print(name, "는 ", str(age), "살이며, ", hobby, "을 아주 좋아해요.") # , 콤마를 쓰면 무조건 씌어쓰기가 포함됌.
print(name + "는 어른일까요? " + str(is_adult_))


### 2-5 주석
''' 작은따음표를 쓰면
여러 라인에
주석처리가 가능하다
ctrl + / 를 하면 여러줄을 한꺼번에 주석처리 가능하다'''