x='x'
while True:
    num=input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요 : ')
    if num=='x':
        print('종료합니다')
        break
    elif num%2==0:
        continue
    elif num%2!=0:
        print(num,'은 홀수입니다.')

while True:
    s=input('숫자(정수)만 입력하세요. 종료를 원하면 x를 입력하세요. : ')
    if s=='x':
        print('종료합니다')
        break
    if int(s)%2==0:
        continue
    else:
        print(s,'는 홀수 입니다.')