email=input('이메일 입력 : ')

if( email.find('@')==-1 or # @ 없는 경우
    email.find('.')==-1 or # . 없는 경우
    email.index('@')>email.index('.') or # @와.의 위치가 바뀐 경우
    email.index('.')-email.index('@')<2 or  # @와. 사이에 문자가 없는 경우
    email.index('@')==0 or # @ 앞에 문자가 없는 경우
    len(email)-email.index('.')<=1 or# . 뒤에 문자가 있을경우
    email.count('@')>=2 or # @ 2개 있는 경우
    email.count('.')>=2 # . 2개 있는 경우
):
    print('이메일 형식이 아닙니다.')

print('입력한 이메일 :',email)