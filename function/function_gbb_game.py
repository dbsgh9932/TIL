from random import randint

def gbb_game():
    a=int(input('You 입력 (1:가위 2:바위 3:보) : '))
    n=randint(1,3)
    if (a==1 and n==3) or (a==2 and n==1) or (a==3 and n==2):
        print('당신이 이겼습니다.')
    elif a==n:
        print('비겼습니다.')
    else:
        print('컴퓨터가 이겼습니다.')
    print('COM : %d' % n)
gbb_game()