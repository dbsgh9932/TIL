def sub(x,y): # 매개변수 x,y -> 지역변수 x=3 y=4
    global a

    a=7 # 전역변수
    x,y=y,x
    b=3 # 지역변수
    print(a,b,x,y)

a,b,x,y=1,2,3,4 # 모두 전역변수
sub(x,y)
print(a,b,x,y) # ->a는 전역변수7 함수 내부b,x,y는 지역변수이므로 함수 외부에서는 b=2 x=3 y=4

# 전역변수a가 생성되어 있어도 지역변수 a를 생성해서 함수 내부에서만 사용 할 수 있다.

def test(a,b):
    x=10 # 지역변수
    a=3 # 지역변수
    b=5 # 지역변수
    print(x,y,a,b) # y는 전역변수사용(외부에서 y=10 정의)

a,b,x,y=5,6,9,10
test(a,b)
a=x*y
print(x,y,a,b)
