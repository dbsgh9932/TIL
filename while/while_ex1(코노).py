x=0
y=2000
z=10000
while x<=5:
    x+=1
    print('노래를',x,'곡 불렀습니다')
    z-=y
    if z==0:
        print('잔액이 없습니다. 종료합니다.')
        break
    print('현재',z,'원 남았습니다.')

print(list(range(1,10)))
