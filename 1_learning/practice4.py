### 5-1 리스트(list)
# 리스트 []
# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨는 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨는 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) 
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list =  ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)


### 5-2 사전(dictionary)
cabinet = {3:"유재석", 100:"김태호"} # key & value
print(cabinet[3])
print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) # 오류 발생 시키고 프로그램 종료
# print("hi")

print(cabinet.get(5)) # none 으로 출력 하고 계속 진행
print("hi")

print(cabinet.get(5, "사용 가능")) # 5번에 "사용 가능" 값을 추가 그리고 출력
print("hi")

#  key가 해당된 dictionary 안에 있나 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"} # key는 integer만 아니라 string도 됌
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 이미 해당된 key에 value 가 있으면 덮어 씌우기
cabinet["C-20"] = "조세호" 
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
# key 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet) # 빈 값을 출력


### 5-3 튜플(tuple)
#list랑은 다르게 내용 변경이나 추가 불가능
menu = ("돈까스", "치즈까스")
print(menu)
print(menu[0])
print(menu[1])

# menu.add("생선까스") add라는 기능을 제공하지 않는다 그러므로 변강 추가 불가능, 고정된 값만 사용 가능

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


### 5-4 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊었어요
java.remove("김태호")
print(java)


### 5-5 자료구조의 변경
coffee = {"커피", "우유", "주스"}
print(coffee, type(coffee))

coffee = list(coffee)
print(coffee, type(coffee))

coffee = tuple(coffee)
print(coffee, type(coffee))

coffee = set(coffee)
print(coffee, type(coffee))
