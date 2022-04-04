'''
# 클로저 사용하기
from re import I


def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환
 
c = calc() # c에 저장된 함수가 '클로저'
print(c(1), c(2), c(3), c(4), c(5))

# 클로저란 함수를 둘러싼 환경을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수를 나타냄

def calc():
    a = 3
    b = 5
    return lambda x: a * x + b

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

# 33.6

def countdown(n):
    i=n+1
    def c():
        nonlocal i
        i -= 1
        return i
    return c


n = int(input())
 
c = countdown(n)

for i in range(n):
    print(c(), end=' ')

# 클래스 사용하기
# 객체지향 프로그래밍이란 복잡한 문제를 잘게 나누어 객체로 만들고 객체를 조합해 문제를 해결
class Person:
    def greeting(self):
        print('Hello')

james = Person() # 클래스는 특정 개념을 표현만 할뿐 사용하려면 인스턴스 생성해야

james.greeting() # 인스턴스 메서드

# 속성 사용하기
class Person:
    def __init__(self):             # initialize 인스턴스(객체) 초기화
        self.hello = '안녕하세요.'
    
    def greeting(self):
        print(self.hello)

james = Person()
james.greeting()

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
 
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    # 안녕하세요. 저는 마리아입니다.
 
print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동

# __slots__ 에 허용할 속성 이름을 리스트로 넣어주면 다른 속성 제한 가능
'
# 비공개 속성 사용하기: __속성 
class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
    def pay(self, amount):
        self.__wallet -= amount   # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))
        if amount > self.__wallet:    # 사용하려고 하는 금액보다 지갑에 든 돈이 적을 때
            print('돈이 모자라네...')
            return
        self.__wallet -= amount
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(13000)
'
class knight():
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    
    def tibbers(self):
        print('티버: 피해량 {0}'.format(self.ability_power * 0.65 + 400))

health, mana, ability_power = map(float, input().split())
 
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
'''
# 클래스 속성과 인스턴스 속성
class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

