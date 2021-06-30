# 정수
a=0b1010 #2진수
b=300 #10진수
c=0o123 #8진수
d=0x12fc #16진수

print(a,b,c,d)

# 실수
f=3.14
f1=1234.45
f2=1.234567e5

print(f,f1,f2)

# 문자열
char1='A'
char2='B'
print(char1,char2)
str1='홍길동'
str2='Python'
str3="""Python Programing"""
str4='''파이썬 프로그래밍'''

str5='''여러줄로
나누어서
사용 가능'''
print(str5)

# 논리값/특수 리터럴
t=True
f=False
print(t,f)

val=None
val1=''
print(type(val),type(val1)) # type()->형식 표현

# 한 줄의 코드를 여러줄로 나눠서 표현하고자 할 때 \or()사용
a=1+2+3+\
4+5+6
b=(1+2+3
   +4+5+6)
print(a,b)

# print함수를 이용해서 문자열을 출력하고자 할 때 여러행 입력
print('긴 문장을 입력 할 때 엔터를 치면'
      '다음 행으로 이동 후 자동으로 따옴표 처리'
      '단, 한 줄로 인식')
print('긴 문장을 입력 할 때 엔터를 치면\n'
      '다음 행으로 이동 후 자동으로 따옴표 처리\n'
      '단, 한 줄로 인식') # \n처리 시 줄 바꿈
print('한 줄에');print('두 개의 명령어') # 한 행에 2개의 명령어 사용 시 ; 입력, 단 줄은 바뀜

