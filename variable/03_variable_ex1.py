name='홍길동'
no=2016001
year=4
grade='A'
average=93.5
level=10

print('성명 :',name)
print('학번 : '+str(no))
print('학년 : '+str(year))
print('학점 :',grade)
print('평균 : '+str(average))

# 포맷코드 사용 (%표시는 %%(그 자체를 표기))
print('성명 : %s'%name)
print('학번 : %d'%no)
print('학년 : %d'%year)
print('학점 : %c'%grade)
print('평균 : %.1f'%average)
print('등급 : %d%%'%level)
