# 튜플 (Tuple)
# 리스트와 유사한 집합적 자료형이지만
# 리스트와 달리 원소 변경 불가
# 추가 / 수정 / 삭제 다 안 됨
# 소괄호 () 사용
# 튜플 = (값1, 값2, … , 값n)
# colors = ("red", "green", "blue")
# numbers = (1, 2, 3, 4, 5 )
# 각 원소는 인덱스(Index)로 구분(인덱스: 0부터 시작)
# 원소 변경 시 에러
# numbers[0] = 10 #오류

# 튜플
t1=(1,2,3)
print(t1)

list1=[1,2,3,t1]
print(list1)

list1[3]=10
print(list1)

t2=4,5,6 # 괄호 없어도 튜플로 생성
print(t2)

t3=t1,7,8,9 # 튜플 내에 다른 튜플 포함 가능
print(t3)

t4=[1,2],[3,4] # 리스트로 튜플 생성
print(t4)

t4_1=3
print(t4_1)
print(type(t4_1)) # type = int

t5=tuple([5,6,7,8]) # 리스트형을 튜플형으로 형변환
print(t5)
print(type(t5)) # type = tuple
print('---------------------------')

# 튜플을 리스트로 변환
# (1,2,3)->[1,2,3)
t1=1,2,3
to_list1=list(t1)
print(to_list1)

# 튜플 내 튜플 원소는 튜플로 유지
t3=((1,2,3),(7,8,9))
to_list2=list(t3)
print(to_list2)

# 리스트를 튜플로 변환
list=[1,2,3]
to_tuple=tuple(list)
print(to_tuple)
