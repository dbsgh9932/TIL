
day=eval(input('총 수강 일수 : '))
needday=day*0.8
print('필요한 최소 수강 일 수 : %.0f' %needday)
myday=eval(input('내가 들은 일수 : '))

price=myday/day

if price>=0.8:
    if myday>=20:
        print(300000,'원')
    else:
        print(myday*15000,'원')
else:
    print('못받음')
