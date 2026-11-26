import sys

print(1 + 2)
print(3 / 2.4)
print(3 * 9)

a = 1
b = 2
print(a + b)

a = "Python"
print(a)

a = 3
if a > 1:
  print("a is greater than 1")

for a in [1, 2, 3]:
  print(a)

i = 0
while i < 3:
  i = i + 1
  print(i)

def add(a, b):
  return a + b

print(add(3, 4))

# 이건 주석입니다.

print("Hello, World!")

"""
이건 여러줄 주석입니다.
"""

sys.exit()