# 매개변수(파라미터)와 반환값이 있는 함수 정의
# 함수 이름 : get_average(k,e,m)
# 파라미터 변수 3개의 값에 대한 평균을 계산한 후 계산된 평균을 반환

# 함수테스트
# 사용자로부터 국어,영어,수학 점수를 입력받아
# get_average(k,e,m) 함수를 호출해서 평균값을 반환받고 출력

def get_average(k,e,m):
    return (k + e + m) / 3
k=int(input('국어 점수 : '))
e=int(input('영어 점수 : '))
m=int(input('수학 점수 : '))

print('평균 : %.2f'%get_average(k,e,m))