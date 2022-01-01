class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable): # super 사용시에 다중 상속을 사용하면 순차대로 뒤에있는 건 상속이 안되게 됌
    def __init__(self):
        super().__init__() # 마지막에 호출되는 함수에만 초기화가 된다
        # 위 같은 상황을 피하기 위해 2번을 통해서 초기화하는 방법이 있음 
        Unit().__init__(self)
        Flyable().__init__(self)

# 드랍쉽
dropship = FlyableUnit() # 어떤 유닛으로 생성 되는지 확인


