n=[1,2,3,3,4,5,4,3]
n.remove(4) # 4 제거 후 원본 반영
print(n)
# 원소값이 3인 원소 모두 제거
count=n.count(3)
for i in range(count):
    n.remove(3)
    print('3삭제 : ',n)
print(n)

# pop() : 리스트 마지막 요소 반환 하고 삭제
x=['a','b','c','d']
y=x.pop()
print(y) # 반환된 마지막요소 d
print(x) # d가 삭제된 리스트 - 원본 반영
print('----------------------------')
x.pop() # c 제거
print(x)
x.pop() # b 제거
print(x)
x.pop() # a 제거
print(x) # 빈 리스트

# x가 빈 리스트인 경우 pop()
# x.pop()
# print(x) # IndexError: pop from empty list - 이미 비어있음

# pop(인덱스) : 인덱스 위치에 있는 요소 반환 후 삭제
heroes=['슈퍼맨','스파이더맨','헐크','아이언맨','배트맨']
temp=heroes.pop(2)
print(heroes)
print('삭제된 값 : ',temp)
