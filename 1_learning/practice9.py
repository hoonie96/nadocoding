# 9-1 예외처리
# 오류가 떠서 프로그램이 종료가 되는 걸 방지하기 위해서
# try 내부에 있는 문장들이 잘 실행이 되다가 뭔가 문제가 발생했을 때
# except 부분에서 오류로 정해둔 것들을 찾으면 해당하는 문구를 실행
# try:
#     print("나누기 전용 계산기입니다.")
#     # num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     # num2 = int(input("두번째 숫자를 입력하세요 : "))
#     # print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError: # int 가 아닌 다른 input 이 주워 졌을때
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err: # 에러에 해당된 문구를 err로 저장
#     print(err) # 프로그램 에러가 아닌 그대로 프로그램 안에서 출력
# except Exception as err: # 나머지 모든 에러들을 출력
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)


# 9-2 에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if  num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


# 9-3 사용자 정의 예외처리
#파이썬에서 이미 제공 하는 에러 말고 직정 정의해서 에러 만들기
class BigNumberError(Exception): # Exception 클래스 상속받고
    def __init__(self, msg): # 이 에러가 발생했을때 메세지를 넣고 싶을때
        self.msg = msg # 2 여기로 던저 주고

    def __str__(self):
        return self.msg # 3 가지고 있다가

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if  num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 1 이 에러가 발생 했을 때 정의한 메시지를
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err: # 4 이쪽에서 처리가 될 때
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err) # 5 여기서 출력


# 9-4 finally
# 에러와 상관없이 무조건 finally 문을 실행 하게 해줌
# 없는 파일을 열려고 한다던지 list 의 없는 값을 잘못 접근한다던지
# 이런 문제가 발생했는데 처리해서 프로그램이 강제 종료되는걸 막음으로서 완성도를 높일 수 있음
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
