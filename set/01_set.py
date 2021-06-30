# 집합 만들기 : {} 이용
s1={1,2,3,4,5}
print(s1)
print(type(s1));print() # class = set

# set() 함수로 집합 만들기
s2=set([10,20,30]) # list형을 set형태로 형변환
print(s2)
print(type(s2));print()

s3=set((100,200,300)) # tuple형을 set형태로 형변환 - {200,100,300} 으로 나오는 이유는 set은 순서가 없음 랜덤임
print(s3)
print(type(s3));print('---------------')

s4={1,2,3,3,4} # 중복값 set에 저장 시 에러안남
print(s4) # 중복값은 한번만 저장 -> {1,2,3,4}

# {}이용해서 리스트를 집합에 추가 시 에러 {}속{}도 에러
# s5={1,2[3,4]} or {1,2,{3,4}} 둘다 에러
# 인덱스 사용불가 print(s4[0]) -> set은 순서가 없으므로 인덱스(순서찾기) 불가
print('---------------------------')
# 집합에 요소 추가, add() - 1개의 요소 추가
s={1,2,3}
s.add(4)
print(s)
# 집합에 요소 추가, update() - 여러개 추가
s.update([5,6])
s.update((7,8))
#s.update(5,6) -> 5하나 6하나 1개씩은 못넣음
#s.update(5) -> 단일로 못넣음
print(s)

# 요소제거
s.remove(3)
print(s)

# 전체 요소 삭제
s.clear()
print(s) # set() -> 빈집합을 의미함(요소만 모두 삭제 껍데기는 그대로)

# 집합 삭제
# del s
