sentence=input('문장을 입력하세요 : ')
sen_isalpha=0
sen_isdigit=0
sen_isspace=0
sen_no=0
for x in sentence:
    if x.isalpha()==True:
        sen_isalpha+=1
    elif x.isdigit()==True:
        sen_isdigit+=1
    elif x.isspace()==True:
        sen_isspace+=1
    else:
        sen_no+=1

print('문자 : %d개'%sen_isalpha)
print('숫자 : %d개'%sen_isdigit)
print('스페이스 : %d개'%sen_isspace)
print('기타 : %d개'%sen_no)
