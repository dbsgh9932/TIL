# 리스트 변수 복사
a=[1,2,3]
# a 리스트 값을 b 변수에 복사하시오.(저장하시오)
# 얕은 복사 : 원본을 변경하면 복사본 내용도 변경
b=a
print(b)
print(a)

b[0]=100
print(a)
print(b)
# b원소값을 변경했지만 서로 참조하므로 둘다 1이 100으로 바뀜

# 깊은 복사(deep copy)
# list()함수 또는 deepcopy()함수를 사용하여
# 리스트의 복사본을 새로 생성하여 변환
# 복사본 리스트 원소의 값을 변경해도
# 원본 리스트 원소값은 변경되지 않음

scores=[1,2,3,4,5]
values=list(scores)
print(scores)
print(values)

values[0]=100
print('scores : ',scores)
print('values : ',values) # 깊은복사 list()함수로 원본scores의 1은 100으로 변하지 않음
# deepcopy()함수 : 깊은 복사
# copy 모듈을 import 해야함

import copy
a=['a','b','c']
b=copy.deepcopy(a)
print('b리스트 수정 전')
print(a)
print(b)
b[0]=1
print('b리스트 수정 후')
print(a)
print(b)

