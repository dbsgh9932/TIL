# 키워드 인수 예제

# 학생 정보를 입력받아 학생 dict을 구성하여 반환하는 함수
def student_info(name,age,gender):
    student={'name':name,'age':age,'gender':gender}
    return student

# 함수 테스트
# 함수 호출 시 인수를 넘겨 dict이 제대로 구성되어 반환되는지 출력

print(student_info(name='kim',gender='여',age=23)) # 키워드 인수
print(student_info('lee',20,'남'))
print(student_info('park',gender='남',age=25)) # 위치 인수와 키워드 인수 동시사용

## 주의
# print(student_info(gender='남',age=22,'lee')) -> 위치 인수는 키워드 인수 앞에 사용해야함!!