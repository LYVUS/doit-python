# 특정 문자의 갯수를 세는 count
a = "hobby"
print(a.count("b"))

# 특정 문자의 위치를 알려주는 find
a = "Python is the best choice"
print(a.find("b")) # 처음 나온 위치를 반환
print(a.find("k")) # 없으면 -1 반환

# 특정 문자의 위치를 알려주는 index
a = "Life is too short"
print(a.index("t")) # 처음 나온 위치를 반환
# print(a.index("k")) # 없으면 오류 발생

# 각 문자 사이에 삽입하는 join
print(",".join("abcd"))
print(",".join(["a", "b", "c", "d"])) # 리스트나 튜플도 사용 가능

# 대문자로 바꾸는 upper
a = "hi"
print(a.upper())

# 소문자로 바꾸는 lower
a = "HI"
print(a.lower())

# 공백을 지우는 strip
a = " hi "
print(a.lstrip()) # 왼쪽만
print(a.rstrip()) # 오른쪽만
print(a.strip())

# 문자열을 바꾸는 replace
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열을 나누는 split
print(a.split()) # 공백을 기준으로 나눔

b = "a:b:c:d"
print(b.split(":")) # :를 기준으로 나눔