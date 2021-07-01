# 인수(인자) 와 매개변수

# 인수(인자) : argument
# 함수에게 실제로 전달되는 값
# print('hello')-'hello'가 인수

# 매개변수 : parameter
# 함수를 호출 할 때 전달되는 실제값을 받아 저장하는 변수
# def print(data)

# 파라미터가 있는 함수 정의
# 이름값을 하나 넘겨받아서 해당 이름을 출력하는 함수
def show_name(name):
    print(name)
# 함수 호출
show_name('홍길동')
show_name(123) # 매개변수도 인자값의 형태에 따라 정해짐