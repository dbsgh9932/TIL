email=input('이메일 입력 : ')

print(email.find('@')) # @ 위치 반환
print(email.find('.'))
print((email.count('@')))
print((email.count('.')))

if email.count('@')>=2 or email.count('.')>=2 or email.count('@')==0 or email.count('.')==0:
    # @가 0개 거나 2개 이상이거나 .가 0개 거나 2개 이상이거나
    print('이메일 형식이 아닙니다.')
    print('입력한 이메일',email)