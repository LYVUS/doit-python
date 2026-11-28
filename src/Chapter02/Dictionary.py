# 딕셔너리
dic = {"name" : "Aokumo Rin", "phone" : "01044336234", "birth" : "0503"}
a = {1 : "Hi"}
b = {"a" : [1, 2, 3]}

# 딕셔너리에 쌍 추가하기
a = {1 : "a"}
a[2] = "b" # key 2에 value b 추가
print(a)
a["name"] = "Aokumo Rin"
print(a)
a[3] = [1, 2, 3] # Key에 리스트를 넣을 수는 없음 (튜플은 가능)
print(a)

# 요소 삭제하기
del a[1]
print(a)

# Key로 Value 얻기
grade = {"Rin" : 10, "Toa" : 99}
print(grade["Rin"])
print(grade["Toa"])

# 동일한 Key는 중복되지 않음
a = {1 : "a", 1 : "b"}
print(a) # "a"는 무시됨

# 딕셔너리 관련 함수
dic = {"name" : "Aokumo Rin", "phone" : "01044336234", "birth" : "0503"}
print(dic.keys()) # dict_keys 객체를 반환

# dict_keys는 객체라서 리스트 함수는 사용할 수 없음
for k in dic.keys():
  print(k)

# 리스트로 변환하려면
dicList = list(dic.keys())
print(dicList)

print(dic.values()) # dict_values 객체를 반환
print(dic.items()) # Key와 Value를 튜플로 묶은 값을 dict_items 객체로 반환

# 청소
dic.clear()
print(dic)

dic = {"name" : "Aokumo Rin", "phone" : "01044336234", "birth" : "0503"}
print(dic["name"]) # 키가 존재하지 않으면 오류 발생
print(dic.get("name")) # 키가 존재하지 않으면 None 반환
print(dic.get("foo", "bar")) # 키가 존재하지 않을 때 디폴트값을 줄 수 있음

print("name" in dic) # 특정 Key가 있는지 조사 (있으면 True 반환)

# Quiz
quizDic = {"name" : "홍길동", "birth" : "1128", "age" : 30}