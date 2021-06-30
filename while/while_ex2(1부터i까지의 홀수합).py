x=int(input('마지막 숫자를 입력하세요 : '))
i=0
sum=0

while i!=x:
    for i in range(1,x+1):
        if i%2==1:
             sum+=i
print('1부터 %d 까지의 홀수의 합은 %d입니다.'%(x,sum))

# 풀이
x=int(input('마지막 숫자를 입력하세요 : '))
i=0
sum=0

while i<=x:
    if i%2==1:
        sum+=i
    i+=1
print('1부터',i,'까지의 홀수의 합은',sum,'입니다.')