#단 수 입력 받고 구구단 출력하는 프로그램

#입력 양식
#단 수 입력 : 7

#출력 양식
# 7*1=7
# 7*2=14
# 7*9=63

dan=int(input('단 수 입력 : '))
for x in range(1,10):
    print('%d * %d = %d'%(dan,x,dan*x))

# 2단부터 9단까지 가로로 출력
for x in range(1,10):
    for dan in range(2,10):
        print('%d * %d = %d'%(dan,x,dan*x),end='\t')
    print()