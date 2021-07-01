s=[]
for i in range(3):
    name = input('회원 입력 : ')
    s.append(name)
s=' '.join(s)
print('회원 명단 : ',s)
for a in s:
    print(a,end='')