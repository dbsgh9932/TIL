# len():문자열의 길이를 반환
string='programming'
print(len(string)) # = 11

# count:문자열 내에 들어있는 특정문자(열)의 개수 반환
# 변수(문자열).count('특정문자(열)')
string='programming'
print(string.count('m')) # m=2번
print('programming'.count('m')) # 문자열 도 가능

# find():문자열 내에서 특정 문자열이 존재하는지 여부와 문자열 시작위치를 반환
# 특정 문자열이 존재하면 시작위치값 반환/ 없으면 -1 반환
# 필터링, 문자열 검사,추출 시 사용
# 변수(문자열).find('특정문자(열)')
crawling='Data crawling is fun'
print(crawling.find('fun')) # 17번 째 부터 시작
print(crawling.find('p')) # 없으므로 -1
print(crawling.find('a')) # 맨 첫번째 문자 위치를 반환

# index():문자열 내에서 특정 문자열 시작위치를 반환
print(crawling.index('fun'))
# print(crawling.index('p')) 없는 단어는 에러발생 어쩔수없음
print(crawling.index('a'))

# split():구분자를 기준으로 문자열을 분리
# 나눈 결과를 리스트로 반환
# 구분자:기본 공백
# 구분자 지정:"-",";",....)

string="Python Programming"
string_split=string.split()
print(string_split) # list로 반환

names="홍길동, 이몽룡, 성춘향 ,변학도"
names_split=names.split(',')
print(names_split) # 띄어쓰기 까지 포함

colors='red:blue:yellow:green'
colors_split=colors.split(':')
print(colors_split)

# 문자열과 리스트의 차이
for c in colors_split:
    print(c) # 단어 통째로
for c in colors:
    print(c) # 문자 하나씩 (:포함)

# range()에 list 사용가능
for i in range(0,len(colors_split)): # (0,4)
    print(colors_split[i])

print(type(colors)) # str 문자열
print(type(colors_split)) # list 리스트

# replace():전체 문자열에서 특정 문자열을 찾아 다른 문자열로 변경
# 전체 문자열.replace('찾는 문자열','변경할 문자열')
# 찾는 문자열이 존재하면 변경된 문자열 반환
# 찾는 문자열이 없으면 원래 문자열을 그대로 반환

course='Java Programming'
# Java문자열을 Python으로 변경
print(course.replace('Java','Python')) # 원본은 변경되지 않는다. replace 후 print(course)-> Java Programming 으로 출력됨
print(course.replace('web','Python')) # web이 없으므로 원래 문자열 반환

# join():각 문자 사이의 특정 문자(열)을 삽입
a='aa'
b='bbb'
print(a.join(b)) # a기준으로 b에 넣어라 baabaab
#b-b-b로 구성
print('-'.join(b))
c_str='대한민국' # 대*한*민*국 출력
print('*'.join(c_str))

# 리스트 에서 join() 사용
sep='-'
names=['홍길동','이몽룡','성춘향']
print(sep.join(names)) # 홍길동-이몽룡-성춘향 -> str형태

# upper():모두 대문자로 / lower():모두 소문자로 / capitalize():문장의 첫번째 문자를 대문자로
# title():단어의 첫 단어만 대문자로(나머지는 소문자로)
print('------------------------------------------------')
string='this is MY DOG'
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())

# 공백 제거
# strip():양쪽 공백 제거/ lstrip():왼쪽 공백 제거 / rstrip():오른쪽 공백 제거
s1=' hello '
print(s1.strip())
print(s1.lstrip(),'test')
print('test',s1.rstrip())

# isalpha():문자여부 결과 반환
# isdigit():숫자여부 결과 반환
# isspace():하나의 문자에 대해 공백 여부 결과 반환
# isalnum():문자 또는 숫자 여부 결과 반환
# 모두 True/False로 반환됨

phone=input('전화번호 입력(숫자만) : ')
while True:
    if phone.isdigit():
        print('완료')
        break
    else:
        phone=input('전화번호 입력(숫자만) : ')
        continue

# 스페이스 여부 확인
print(' '.isspace()) # T
print(' c'.isspace()) # F (문자가 있으므로)
print('  '.isspace()) # T
