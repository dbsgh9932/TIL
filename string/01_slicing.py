# 문자열
# 문자들의 나열 - 한 문자당 하나의 메모리공간을 차지한다.
# 'abc' -> a한칸 b한칸 c한칸 공간을 차지하고 공간이 연속되어있음

# 인덱싱과 슬라이싱이 가능 (n번째 호출-인덱싱 n번째부터m부터까지 호출-슬라이싱)
# 문자열 생성- '',"",""""""
crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'
# 전체 문자열 출력(반환)
print(crawling)
print(crawling[:])
# 특정 인덱스 문자 출력 - 파이선이 인덱싱은 0부터 시작
print(crawling[0]) # 첫 번째 문자
print(crawling[-1]) # 마지막 문자

# 슬라이싱 예제
print(crawling[1:4]) # 1부터 3까지 문자
print(crawling[1:4+2])
print(crawling[:-1]) # 처음부터 마지막 전 문자 까지
print(crawling[-1:])
print('-----------------------------------')

print(parsing[5:])
print(parsing[:15])
print(parsing[:])
