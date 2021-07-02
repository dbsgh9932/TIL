# 내장함수

# abs(x) : x의 절대값 반환
print(abs(-10))

print('==all()==')
# all(iterable) : 모든 요소가 참이면 True 아니면  False
# false=0,true!=0인 모든 값
# 즉 0 이 하나라도 있으면 false 반환
# iterable : 각각의 요소를 하나씩 반환할 수 있는 객체/for문으로 반복해서 출력이 가능한 자료형
# 리스트,튜플,집합,딕셔너리
print(all([1,2,3,4]))
print(all([0,1,2,3,4])) # 0이 있으므로 false

print('==any()==')
# any(iterable) : 하나라도 참이면 true 아니면 false
# 전부 0이면 false, 아니면 true
print(any([0,0,0]))
print(any([0,1,0]))
print(any([0,'',[]])) # 0,빈문자열,빈리스트 - false

print('==chr()==')
# chr(i) : 아스키코드값에 해당하는 문자 반환
print(chr(65))
print(chr(97))
print(chr(13))

for i in range(65,100):
    print(chr(i))

print('==ord()==')
# ord : chr와 반대로 문자에 해당되는 아스키코드값 반환
print(ord('a'))
print(ord('o'))
print(ord('\n'))
print(ord(' '))
print(ord('\r'))

print('==divmod==')
# divmod(a,b) : a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print(divmod(7,3))

