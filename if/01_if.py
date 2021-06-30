password=1234

# if password==1234 :
#     print('비밀번호가 일치합니다.') #if문 내부
# print('끝') #if문 종료 후 실행

if password==1234:
    print('비밀번호가 일치합니다.') #if문 내부
else:
    print('비밀번호가 일치하지 않습니다.') #else문 내부

print('끝')

#else문이나 if문에서 아무것도 수행하지 않게 하려면

if password==1234:
    print('비밀번호가 일치합니다.')
else:
    pass #어떤것도 수행없이 문장종료
