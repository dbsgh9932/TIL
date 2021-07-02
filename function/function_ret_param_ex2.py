def get_interest():
    a=eval(input('예금액 입력 : '))
    b=eval(input('이자율 입력(%) : '))
    return a*b/100
print('이자액 : %d원'%get_interest())
