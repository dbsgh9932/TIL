# 화씨 온도를 섭씨 온도로 변환하는 예제
ftemp=90 # 정수 변수
ctemp=(ftemp-32)*5/9 #정수 연산
#ctemp의 type은 실수

print(ctemp)
print('%f'%ctemp)
print('%.3f'%ctemp)
# 실수 %f 사용시 %전체자리수.소수이하자리수f
print('%10.3f'%ctemp) # 소수점 포함 10자리


# 2개 이상의 포맷문자에 대한 변수입력 -> %(a,b....)
print('화씨온도 %d 를 섭씨온도로 변환하면 %.3f 입니다.'%(ftemp,ctemp))