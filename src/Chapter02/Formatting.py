# 문자열 포매팅
a = "I eat %d apples." % 3
print(a)

a = "I eat %s apples." % "five"
print(a)

number = 3
a = "I eat %d apples." % number
print(a)

# 값이 2개 이상인 경우
number = 10
day = "three"

a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

# %를 그대로 쓰려면 %%
a = "Error is %d%%." % 98
print(a)

# 포맷 코드 활용
print("%10s" % "hi") # 10칸 안에서 오른쪽 정렬
print("%-10sjane" % "hi") # 10칸 안에서 왼쪽 정렬
print("%0.4f" % 3.42134234) # 소수점 4번째 자리까지
print("%10.4f" % 3.42134234) # 10칸 안에서 소수점 4번째 자리까지 오른쪽 정렬

# format 함수
print("I eat {0} apples.".format(3))
print("I eat {0} apples.".format("five"))

number = 3
print("I eat {0} apples.".format(number))

# 두 개 이상의 값
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3))

# 인덱스와 이름 혼용
print("I ate {0} apples. so I was sick for {day} days.".format(10, day = 3))

# 정렬
print("{0:<10}".format("hi")) # 왼쪽 정렬
print("{0:>10}".format("hi")) # 오른쪽 정렬
print("{0:^10}".format("hi")) # 가운데 정렬
print("{0:=^10}".format("hi")) # 공백을 =로 채우며 가운데 정렬
print("{0:!<10}".format("hi")) # 공백을 !로 채우며 왼쪽 정렬

# 소수점 표현
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

# { }를 그대로 쓸 경우 {{ }}
print("{{ and }}".format())

# f 문자열 포매팅 (3.6버전 이후)
name = "아오쿠모 린"
age = 18
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")

# f 문자열 포매팅은 표현식을 지원함
print(f"나는 내년이면 {age + 1}살이 된다.")

# 딕셔너리도 지원함
d = {"name" : "아오쿠모 린", "age" : 18}
print(f"나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.")

# 정렬도 지원함
print(f"{"hi":<10}")
print(f"{"hi":>10}")
print(f"{"hi":^10}")
print(f"{"hi":=^10}")
print(f"{"hi":!<10}")

# 소수점도 지원함
y = 3.42134234
print(f"{y:0.4f}")
print(f"{y:10.4f}")

# { } 를 그대로 쓰려면
print(f"{{ and }}")

# Quiz
print(f"{"python":!^12}")