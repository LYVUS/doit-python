# 집합
s1 = set([1, 2, 3])
s2 = set("Hello")
print(s2) # 중복을 허용하지 않고, 순서가 없음

# 인덱싱으로 접근하려면 리스트나 튜플로 변환
l1 = list(s1)
print(l1)
t1 = tuple(s1)
print(t1)

# 집합 연산
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1.intersection(s2))
print(s1 & s2) # &을 사용해 간단하게

# 합집합
print(s1.union(s2))
print(s1 | s2) # |을 사용해 간단하게

# 차집합
print(s1.difference(s2))
print(s2.difference(s1))
print(s1 - s2) # -를 사용해 간단하게
print(s2 - s1)

# 집합 함수
s1 = set([1, 2, 3])
s1.add(4) # 요소 추가
print(s1)
s1.update([5, 6]) # 요소 다수 추가
print(s1)

s1.remove(2) # 요소 제거
print(s1)