#1000초는 몇분 몇초인가
seconds=1000
minutes=seconds//60
remainder=seconds%60
print(minutes,remainder)

seconds=input('초는')

print('%d분 %d초'%(minutes,remainder))
