# 불: True or False
a = True
b = False # 첫 문자는 대문자로

print(type(a)) # 'bool' 타입을 확인

# 조건문의 반환값으로 사용됨
print(1 == 1) # True
print(2 > 1)
print(2 < 1)

# 자료형의 Falsy들
f1 = ""
f2 = []
f3 = ()
f4 = {}
f5 = 0
f6 = None

a = [1, 2, 3, 4] # a는 Truthy
while a: # a가 빈 리스트가 되면 Falsy가 되어 조건문을 빠져나옴
  print(a.pop()) 

# 불린 함수
print(bool("python"))
print(bool(""))