# print() : 화면에 결과를 출력
age=25
print('나는',age,'살 입니다')
print('나는 '+str(age)+'살 입니다')
print('나는 %d살 입니다'%age)

# 변수와 값이 다음과 같을 때
# 총점과 평균을 구해서
# 아래와 같이 출력(포맷코드사용)
kor,eng,math=90,80,80
total=kor+eng+math
avg=total/3
print('총점 : %d'%total)
print('평균 : %.2f'%avg)
print('총점 : %d, 평균 : %.2f'%(total,avg))