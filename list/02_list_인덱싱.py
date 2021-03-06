# 특정 원소에 접근 : 인덱싱
# 리스트에서 인덱싱 연산자를 통하여 요소를 참조(접근)하는 것

a=[1,2,3,4,5] # 인덱스로 음수를 사용 할 수 있다
print(a[0])
print(a[-1])
print(a[-2])

b=[1,2,3,[10,20]]
print(b[-1]) # [10,20]
print(b[-1][0]) # [10,20] 에서 첫 번째인 10이 나옴

c=[1,3,[5,6],8]
# 원소값 6을 출력
print(c[2][1])

d= [1,2,3,[4,5,[7,8]],2]
# 원소값 8을 출력
print(d[-2][-1][1])

# 각각의 리스트를 리스트화 할 수 있다.
a=[1,2,3,4,5]
b=[1,2,3,[10,20]]
c=[1,2,3,[10,20],4,5]
all_list=[a,b,c]
print(all_list)