# # 10-1 모듈 (module)
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(3) # 4명이서 조조 할인 영화 보러 갔을 때 가격
# theater_module.price_soldier(3) # 5명의 군인이 영화 보러 갔을 때 가격

# # as 를 붙이고 이름을 정함으로써 위에처럼 전체를 안적어도 되겠끔 간편히 사용가능
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# # 여기 모듈에 있는 모든 걸을 import 해서 사용 하겠다.
# # 더 짦아져서 간편 하지만 구분이 어려울 수 있음
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# # 필요한 함수만 명시 해서 가져올 수 있음
# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5) # import 를 안 했기 때문에 NameError: 'price_soldier' not defined

# # # 필요한 함수만 명시 해서 가져오고 별명을 칭해서 사용 가능
# from theater_module import price_soldier as price
# price(5) # 일반 가격이 아닌 군인 가격을 price 로 명시 후 가져오기 때문에 군인 가격 출력


# # 10-2 패키지 (package)
# import travel.thailand # 맨 뒤는 모듈이나 패키지만 가능함. 클래스나 함수는 import 직접 불가능.
# import travel.thailand.ThailandPackage() # ModuleNotFoundError
# trip_to = travel.thail #and.ThailandPackage()
# trip_to.detail()

# 아래와 같이도 import 가능
# from travel.thailand import ThailandPackage # 패키지에서 모듈의 클래스를 가져오기
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# # 10-3 __all__
# #from travel import * # * 이 from random import * 처럼 전체를 가져오진 않음
# from travel import * # 하지만 개발자가 공개 범위를 설정해줘야 함. __init__.py 가서 __all__ 에 리스트 설정을 해주면 가능.
# # trip_to = vietnam.VietnamPackage()
# # trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


# 10-4 모듈 직접 실행
# travel.thailand.py 확인


# # 10-5 패키지, 모듈 위치
# import inspect
# import random

# from travel import *
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


# 10-6 pip install
# pypi 에서 여러 프로젝트 확인해볼 수 있음
# pip install packageName # pip 을 이용해 다운 받아서 해당된 모듈의 패키지 이용 가능.
# pip show packageName # 상세한 정보 보여줌
# pip install --upgrade packageName # 업그레이드 할 버젼이 있으면 업그레이드 가능
# pip uninstall packageName # 내용을 삭제하고 싶을 때


# 10-7 내장함수 (builtin functions)
# # input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다.".format(language))

# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())

# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# google 'list of python builtins' and you can check all info


# 10-8 외장함수
# google 'python module index' and you can check all info

# # glob : 경로 내의 폴더 / 파일 목ㄱ록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공 하는 기본 기능
# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# # time : 시간 관련 함수 
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘 부터 100일 후