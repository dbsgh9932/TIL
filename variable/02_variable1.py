# 변수는 할당해놓고 사용하지 않으면 메모리 공간을 차지하게 됨
# 변수를 삭제하는 명령어 del
# del 변수명

# c_var=100
# print(c_var)
# del c_var
# print(c_var)
# 코드 블럭 주석처리 : ctrl+/

# 문자열 값저장
# 문자열을 큰따옴표 사용 (작은따옴표 사용가능)
# 여러 종류의 따옴표를 사용시에는 짝을 맞춰야 함
name="홍길동"
std_name="김철수"
pro_name="이몽룡'교수'"
print(name)
print(std_name)
print(pro_name)
print(name,std_name,pro_name)

# 문자열 연결하는 작업 : + 연산자
address='서울시 강남구'
print(name,address)
print(name+address)

print(name+'은 '+address+'에 삽니다')
result=name+'은 '+address+'에 삽니다'
print(result)

# 문자와 숫자의 결합(연결)
age=23

print(name + '은 '+str(age)+'살 입니다')
# 홍길동은 23살 입니다.
# 값은 숫자형이지만 문자열로 처리해야 할 때는 일시적으로 형태(type)를 변경함
# 숫자 -> 문자 str(변수명)
print(5 + age)

# 사각형의 면적을 구해서 출력하는 프로그램
# 넓이:100
# 높이:200
width=100
height=200
area=width*height
print('면적 : '+str(area))
print('면적 :',area)

# print()함수에서 문자열과 변수를 함께 출력할 때
# print("문자열", 변수)
# or 포맷코드사용
# print('서식'%값)
# print('문자열 %d 문자열'% 변수)
# print('나이: %d 살' % age)
# print('내이름은 %s 입니다' % name)
age=75
print('나이 : %d 살' % age)
