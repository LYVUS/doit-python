# 문자열 더하기 (Concatenation)
head = "Python"
tail = " is fun!"

print(head + tail)

# 문자열 반복
a = "Python"
print(a * 3)

# 문자열 길이 함수
b = "Life is too short"
print(len(b))

c = "You need python"
print(len(c))

# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])
print(a[0])
print(a[12])

print(a[-1]) # -를 붙이면 뒤에서부터 읽음
print(a[-2])
print(a[-5])

# 문자열 슬라이싱
b = a[0] + a[1] + a[2] + a[3]
print(b)

# 슬라이싱 기법
print(a[0:4])
print(a[5:7])
print(a[12:17])

print(a[19:]) # 생략시 끝까지
print(a[:17]) # 생략시 처음부터
print(a[:])
print(a[19:-7]) # 음수도 사용 가능

# 응용
a = "20010331Rainy"

date = a[:8]
weather = a[8:]

print(date)
print(weather)

# 문자열은 불변형
a = "Pithon"
# a[1] = "y" # 불가능
print(a[:1] + "y" + a[2:])