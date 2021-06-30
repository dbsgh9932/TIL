a=int(input('숫자1 입력 : '))
b=int(input('숫자2 입력 : '))

sumx=0
for x in range(a,b+1):
    sumx+=x
print(a,'부터',b,'까지의 합 :',sumx)