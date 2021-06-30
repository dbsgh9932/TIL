a=[1,2,3,4,5]
# len() - 리스트의 길이반환
print(len(a)) # 5
# count() - 리스트 내 특정요소 갯수 / 리스트.count(특정요소)
print(a.count(3)) # 1
# append() - 리스트의 끝에 새로운 요소 추가 / 리스트.append(새로 추가할 요소)
# insert() - 리스트의 특정 위치에 요소 삽입 /  리스트.insert(삽입위치,새로 추가할 요소)
# remove() - 리스트에서 값에 해당하는 요소 제거 / 리스트.remove(제거할 요소값) 동일값 존재 시 첫 번째 값만 제거
# 동일값 제거하려면 for문 사용
# pop() - 리스트의 마지막 요소 반환하고 삭제 - 리스트.pop() / 인덱스 위치에 있는 요소 반환하고 삭제 - 리스트.pop(인덱스값)
# extend() - 리스트의 확장 / 리스트.extend()
a=[1,2,3]
a.extend([4,5])
print(a) # 원소가 추가되지만 하나의 리스트 [1,2,3,4,5]
b=[1,2,3]
b.append([4,5])
print(b) # 원소가 하위리스트로 추가됨 [1,2,3,[4,5]]

# sort() - 원소의 정렬과 관련된 함수
# reverse() - 원소의 정렬과 관련된 함수
# sorted() - 원소의 정렬과 관련된 함수

# index() - 리스트 안에서 원소의 위치값 반환 / 리스트.index(값)
a=[1,2,3,4,5,5]
print(a.index(3))
print(a.index(5)) # 중복값 존재 시 첫 번째 값 위치를 반환
# print(a.index(10)) # ValueError: 10 is not in list - 10이 없으므로 에러발생
print('-----------------')
# min() - 리스트 내에서 최소값 원소 반환 /
# max() - 리스트 내에서 최대값 원소 반환 /
n=[100,7,-2,99,30]
char=['c','a','D','A','b']
n_char=[1,100,'a','D',-2]

print(min(n))
print(min(char))
# print(min(n_char))
print('---------------------')
print(max(n))
# print(max(char))
# 문자,숫자 복합 자료형은 대소비교 불가

# in/not in (포함여부 판단 후 True/False로 반환)
num=[1,2,3,4,5]
result=2 in num # 2가 있나?
print(result)
result=2 not in num # 2가 없나?
print(result)
print('-----------------------')
# 리스트 일치 검사
# 비교 연산자를 사용해서 2개의 리스트 비교 (==,!=,>,>=,<,<=)
# 첫 번째 요소부터 비교 시작
# 첫 번째 요소 비교에서 결과가 false면 비교중지, 첫요소 동일시 두번째요소 비교..
# 리스트 안의 모든 요소 비교 결과가 True면 전체결과:True
list1=[1,2,3]
list2=[3,2,4]
print(list1==list2)

