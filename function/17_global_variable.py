# 전역변수(global variable)
# 함수 외부에서 정의된 변수
# 프로그램 내 모든 곳에서 사용가능
# 함수 내에서 전역 변수의 값을 변경하려면 global 키워드 사용

a=1 # 함수 밖에서 정의된 전역변수a

def show():
    c=a+b
    print(a)
    print(b)
    print(c) # 지역변수

def add():
    print(a)
    print(b)

b=2 # 함수 밖에서 정의된 전역변수b - 모든곳에서 사용가능
print(show())

## 전역변수는 파일 내 어디서든 사용 가능
# 함수 정의 후에 전역변수가 만들어졌어도 사용 가능
# 함수 외부에서 전역변수를 이용해서 실행(처리)할 때
# 실행전에 전역변수가 생성되어 있어야 함
