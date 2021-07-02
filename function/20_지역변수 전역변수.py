# 함수 내부
def var_test(a): # a 지역변수
    a=7
    print(a,'메모리 주소 : ',id(a))
    b=50
    print(b,'메모리 주소 : ',id(b))

# 함수 외부
a=10
b='abc'
var_test(a)
print(a,'메모리 주소 : ',id(a))
print(b,'메모리 주소 : ',id(b))