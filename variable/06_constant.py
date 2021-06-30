# 값이 변경되지 않는 값
# 파이썬에서는 별도의 상수가 없음
# 변수와 구분하기 위해 대문자로 사용
# 나중에 상수의 값을 변경해도 오류 없음

Pi=3.141592
r=10
area=r*r*Pi
print(area)

###############################
INT_RATE=0.03 # 이자율 (상수로 사용하기 위해 할당)
deposit=10000
interest=deposit*INT_RATE
balance=deposit+interest

print(balance)
print(int(balance)) #int->정수형으로 변환
# 천단위 구분기호 사용
print(format(int(balance),',')) #format(값,구분기호) format 사용시 형태가 문자열로 변하므로 %d,%f가 아닌 %s로 표현한다.

INT_RATE='이자율' #값을 변경해도 오류x
#1.234e2=123.4    1.234e-2=0.01234

