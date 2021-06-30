x=int(input('정수1 입력 : '))
y=int(input('정수2 입력 : '))
z=int(input('정수3 입력 : '))

if (x>y and x>z):
    if (y>=z or z>=y):
        print('제일 큰 수 : %d' %x)
if (y>z and y>x):
    if (z>=x or x>=z):
        print('제일 큰 수 : %d' %y)
if (z>x and z>y):
    if (x>=y or y>=x):
        print('제일 큰 수 : %d' %z)

#해설
#1. 정수 3개 입력받아 변수에 저장
a=int(input('정수1 입력 : '))
b=int(input('정수2 입력 : '))
c=int(input('정수3 입력 : '))
#2. 저장된 3개의 변수 중 가장 큰 수 판별
#a가 가장 큰 경우 : a>b and a>c
if a>b and a>c:
    print('제일 큰 수 :',a)
#a가 가장 크지 않은 경우 : b>c->b가 가장 큼
elif b>c:
    print('제일 큰 수 :',b)
#b도 제일 큰 수가 아닌 경우 : c
else:
    print('제일 큰 수 :',c)
#3. 판별된 제일 큰 수가 출력
