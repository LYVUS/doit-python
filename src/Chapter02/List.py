# 리스트
odd = [1, 3, 5, 7, 9]

# 임의의 자료형 모두 포함 가능
a = []
b = [1, 2, 3]
c = ["Life", "is", "too", "short"]
d = [1, 2, "Life", "is"]
e = [1, 2, ["Life", "is"]]

# 인덱싱과 슬라이싱
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1]) # 마지막 요소

a = [1, 2, 3, ["a", "b", "c"]]
print(a[0])
print(a[-1])
print(a[3])

# 리스트에 포함된 리스트에 접근하려면
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])

b = a[:2]
c = a[2:]
print(b)
print(c)

# Quiz
print(a[1:3])

# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(len(a))

# 리스트의 수정과 삭제
a = [1, 2, 3]
a[2] = 4
print(a)

# del 함수로 요소 삭제
a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

# 요소를 추가하는 append
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)

# 리스트를 정렬하는 sort
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ["a", "c", "b"]
a.sort()
print(a)

# 리스트를 뒤집는 reverse
a = ["a", "c", "b"]
a.reverse()
print(a)

# 특정 값의 위치를 반환하는 index (없으면 오류)
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))

# 특정 위치에 요소를 삽입하는 insert
a = [1, 2, 3]
a.insert(0, 4) # index 0에 4 삽입
print(a)
a.insert(3, 5)
print(a)

# 특정 요소를 제거하는 remove
a = [1, 2, 3, 1, 2, 3]
a.remove(3) # 처음 3을 삭제
print(a)

# 마지막 요소를 꺼내고 삭제하는 pop
a = [1, 2, 3]
print(a.pop())
print(a)

a = [1, 2, 3]
print(a.pop(1)) # index를 인수로 주면 해당 값을 꺼내줌
print(a)

# 특정 요소의 갯수를 세주는 count
a = [1, 2, 3, 1]
print(a.count(1))

# 리스트를 확장하는 extend
a = [1, 2, 3]
a.extend([4, 5]) # 뒤에 해당 리스트를 더해줌
print(a)
b = [6, 7]
a.extend(b)
print(a)