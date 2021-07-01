# dictionary 반환
# 함수명 : get_info()
# 함수 기능 : 사용자로부터 이름과 나이를 입력받아 dict으로 저장하고
# 저장된 dict데이터를 반환하는 함수

def get_info():
    name=input('이름 입력 : ')
    age=input('나이 입력 : ')

    student={'name':name,'age':age}
    return student
student_info=get_info()

print(get_info())
print(student_info)
print(type(student_info))

# 함수 테스트
# 함수를 호출하여 반환값을 변수student_info에 저장하고
# 변수값 출력/변수형태 확인