#1부터 10까지 출력하고 1~10까지 더한 결과도 출력하는 프로그램을 작성하시오
#누적합 변수 선언 및 초기화 후 사용
sumx=0
for x in range(1,11):
    print(x)
    sumx+=x
print('1부터 10까지 누적 합',sumx)

#1부터 100까지 더하는 프로그램 작성
sumx=0
for x in range(1,101):
    sumx+=x
print('1부터 100까지의 누적합',sumx)