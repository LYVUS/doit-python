# 문자열 생성 방법 4가지
a = "Hello world" # 큰따옴표
b = 'Python is fun' # 작은따옴표
c = """Life is too short, You need Python""" # 큰따옴표 3개
d = '''Life is too short, You need Python''' # 작은따옴표 3개

# 문자열에 작은따옴표 포함
food = "Python's favorite food is perl" # 큰따옴표로 감싼 후 포함시키기

# 문자열에 큰따옴표 포함
say = '"Python is very easy." he says.' # 작은따옴표로 감싼 후 포함시키기

# 백슬래시 사용
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# 여러 줄 문자열을 변수에 대입하는 방법
line = "Life is too short\nYou need Python" # 이스케이프 코드(\n) 삽입

# 연속 따옴표 사용
multiLine = """
Life is too short
You need Python
"""

print(line)
print(multiLine)