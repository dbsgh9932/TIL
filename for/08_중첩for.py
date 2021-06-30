# 다중 for문 : for문 안에 for문을 포함하는 문장
for y in range(3):# y 0~2
    for x in range(5): # x 0~4
        print(x,end='')
    print()

# print(x,end='')문장 수행 횟수 15번 (x for문을 5번 * y for문을 3번 = 15번)
# print()문장 수행 횟수 3번 (y for문을 3번)

# 1  2  3  4
# 5  6  7  8
# 9  10 11 12 만들기
sumx=0
for y in range(3):
    for x in range(4):
        sumx+=1
        print(sumx,end='   ')
    print()