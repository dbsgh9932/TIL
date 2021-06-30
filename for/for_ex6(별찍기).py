for x in range(4):
    for y in range(5):
        print('*',end='')
    print()

for x in range(5):
    for y in range(5):
        if y<=x:
            print('*',end='')
    print()

for x in range(5):
    for y in range(5):
        if y>=x:
            print('*',end='')
    print()

# 피라미드 형 별 찍기
for x in range(0,5):
    #스페이스 찍기
    for y in range(4,x,-1): # x의 값변화:0,1,2,3,4
        print(' ',end='')
    #별 찍기
    for z in range(0,x*2+1): # 1,3,5,7,9
        print('*',end='')

    print()
# 역피라미드형 별 찍기
for x in range(0,5):
    for y in range(0,x,1):
        print(' ',end='')
    for z in range(9,x*2,-1):
        print('*',end='')
    print()

# n값에 따라(행의 증감에 따라) 찍히는 별도 증감하게 수정
n=10
for x in range(0,n):
    #스페이스 찍기
    for y in range(n-1,x,-1): # x의 값변화:0,1,2,3,4
        print(' ',end='')
    #별 찍기
    for z in range(0,x*2+1): # 1,3,5,7,9
        print('*',end='')

    print()