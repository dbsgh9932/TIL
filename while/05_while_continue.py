# continue문
# 반복문 수행 중 continue를 만나면
# 현재 시점에서 중단하고(다음 문장 실행x)
# 다음 반복 계속 수행

x=0
while x<10:
    x+=1
    if x%2==0:
        continue # 2의 배수 이면 print를 수행하지 않고 while문을 다시 시작
        #break # 2의 배수이면 모든 것을 중단하고 현재 x를 출력 (1을 출력한다.)
    print(x)