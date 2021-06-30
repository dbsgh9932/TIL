day=eval(input('총 수강 일수 : '))
myday=eval(input('내가 들은 일수 : '))
price=myday/day

if price>=0.8:
    if myday>=20:
        print(300000,'원')
    else:
        print(myday*15000,'원')
else:
    print('못받음')