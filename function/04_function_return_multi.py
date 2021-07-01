# 여러개의 값 반환하기
# 파이썬제외 다른 프로그램 언어에서는 함수는 항상 하나의 값만 반환
# 파이썬은 함수가 여러개의 값을 반환 할 수 있음

def multi_return():
    return 1,2,3

a,b,c,=multi_return() # 반환된 여러개의 값을 변수에 저장 -> 여러개의 변수에 저장
print(a,b,c)
print(multi_return()) # 반환된 값을 바로 출력(튜플로 반환)