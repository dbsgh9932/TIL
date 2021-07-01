# for문:정해진 횟수만큼 반복 할 때 주로 사용
# for 반복요소를 저장할 변수 in 반복을 위한 리스트,범위
# 반복1...
# 반복2...

# 리스트['홍길동','이몽룡','성춘향','변학도']의 요소를 모두 출력하시오
s_name=['홍길동','이몽룡','성춘향','변학도']
for name in s_name:
    print(name)

# 위 리스트의 요소들을 각각 출력하시오
# num=[1,2,3,4,5,6,7,8,9]
# for n in num:
#     print(n,end='') #for문 안의 변수와 리스트의 이름이 같아도 무방
# 반복 범위 설정:range()함수
# 특정 범위의 정수 생성
# range(start,stop,step)
# range(10) -> 0~9까지 정수
# range(1,10) -> 1~9까지 정수
# range(1,10,2) -> 1~9까지 1부터 2씩 증가하는 정수

for i in range(10):
    print(i,end='')
for i in range(1,10):
    print(i)
for i in range(1,10,2):
    print(i)