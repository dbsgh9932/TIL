# 전역변수를 함수 내부에서 변경하려면 global 키워드 사용

a=1 # 함수 외부에서 정의된 전역변수a

def add():
    #a=a+1 # 함수 내부에서 지역변수 전역변수 둘이 충돌
    global a # a는 전역변수이고 함수 내에서 수정가능하다는 키워드
    a+=1
    c=a+b
    # print(a)
    # print(b)
    # print(c)

b=3 # 함수 밖에서 정의된 전역변수b - 함수 정의 후 생성되어도 함수 내에서 사용가능

print(a) # 처음a=1
add()
print(a) # 1+1 -> 2
add()
print(a) # 2+1 -> 3