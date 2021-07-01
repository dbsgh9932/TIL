# 딕셔너리
# 키(key)와 값(value)의 한 쌍을 요소로 갖는 자료형
# 딕셔너리 = {키1:값1, 키2:값2, … }
# d = {1:’a’, 2:’b’, 3:’c’}

# 딕셔너리의 특징
# 순서가 없다. 따라서, 인덱스로 접근할 수 없다
# 중괄호 {} 사용
# key를 통해서만 접근
# key는 숫자, 문자 다 가능
# key:value 한 쌍을 item이라고 한다
# 쉼표(,)로 item 구분

# 딕셔너리 만들기 {key:value}
d={1:'a'}
print(d)
print(type(d))

# 두 번째 요소(item) 추가 (key=2,value='b')
d[2]='b' # 딕셔너리에서는 인덱스아님
print(d)
print('---------------------------')

# 세 번째 요소 추가
# key는 문자도 가능
d['test']='value test'
print(d)
print('---------------------------')
member={'name':'홍길동','phone':'1234-1234','birth':'10/15'}
print(member)
member['address']='서울'
print(member)
print('---------------------------')
# 딕셔너리 주요 함수
# 딕셔너리.keys() : key만 추출해서 리스트로 반환
# [1, 2, 3]
# 딕셔너리.values() : value만 추출 리스트로 반환
# [‘a’, ‘b’, ‘c’]
# 딕셔너리.items() :
# (key:value)의 튜플을 추출해서 리스트로 반환
# [(1:’a’), (2:’b’), (3:’3’)]

print(member.keys()) # key리스트
print(member.values()) # value리스트
print(member.items()) # (key:value)리스트
print('---------------------------')

# 리스트로 변환 : list()함수 사용 / 튜플로 변환 : tuple()함수 이용
to_list=list(member.keys())
print(to_list)

to_tuple=tuple(member.keys())
print(to_tuple)
print('---------------------------')
# 특정 item value 참조 : key이용
print(member['name'])
print('---------------------------')

# key리스트의 각 요소 출력
for key in member.keys():
    print(key)
print('---------------------------')
# value값 출력
for value in member.values():
    print(value)
print('---------------------------')
# item 출력
for item in member.items():
    print(item)
print('---------------------------')

# key로 value값 찾기         a['key'] / a.get('key')
print(member['name'])
print(member.get('birth'))

# 존재하지 않을 경우
# print(member['time']) error
print(member.get('time')) # none값 반환

# if문에서 get() 사용
insert_key='link'
if member.get(insert_key) is None:
    print(insert_key+'에 대한 data가 없습니다')

# 존재 여부만 확인 : in ' not in
print('link'in member)
print('link'not in member)

# list/dict/tuple 관련 함수 확인 : dir() 사용
my_list=[]
print(dir(my_list))
my_tuple=()
print(dir(my_tuple))
my_dict={}
print(dir(my_dict))