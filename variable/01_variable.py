# 변수의 값을 저장
# 변수=값
result = 10
print(result) # 화면에 변수값을 출력하는 명령어

result = 'a'
print(result)

# 여러개의 변수에 여러개의 값을 한번에 저장 가능
# 변수1, 변수2, 변수3,...=값1, 값2, 값3
# 파이썬 코드는 맨 앞칸에서 시작 (공백x)
a,b,c,d=1,2,3,4
print(a)
print(b)
print(c)
print(d)

# 변수이름 = 실제값이나 값이 들어있는 식별자도 가능
e,f,g=a,b,c

a,b=10,20 #a,b 값은? 10 20
print(a)
a,b=b,a #a,b 값은? 20 10
print(a)