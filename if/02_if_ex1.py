id=input('아이디 입력 : ')
pwd=eval(input('비밀번호 입력 : '))

if (id=='flower' and pwd==int(1234)):
    print('로그인 성공!')
else:
    print('로그인 실패!')