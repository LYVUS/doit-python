# 변수
a = 1
b = "Python"
c = [1, 2, 3] # 파이썬은 자료형을 스스로 판단해 지정해줌

# 변수의 메모리 주소값 확인
print(id(a))

# 동일 객체 참조
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b) # 동일 객체 판단

a[1] = 4
print(a)
print(b) # 동일 객체이므로 b도 똑같이 변함

# 객체 복사 방법
a = [1, 2, 3]
b = a[:] # 참조값이 다른 객체를 새로 복사해 생성
print(id(a))
print(id(b))

a[1] = 4
print(a)
print(b) # 다른 객체이므로 b는 영향을 받지 않음

# copy 모듈 활용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a)
print(b)
print(a is b) # False

# 변수 동시 생성 방법
a, b = ("Python", "Life") # 튜플 활용
a, b = "Python", "Life" # 괄호 생략 가능
print(a)
print(b)

a, b = ["Python", "Life"]
a = b = "Python"

# 두 변수의 값을 서로 바꾸는 간단한 방법
a = 3
b = 5
a, b = b, a
print(a)
print(b)

# Quiz
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False: 서로 별도로 선언했기 때문에