#파이선에서 난수(random number)를 사용하기 위해선 기본적으로 제공되는 random모듈 사용
#randint(최소,최대)
#최소부터 최대 사이의 임의 정수 반환

from random import randint #random모듈의 randint함수사용준비
# n=randint(1,100) -> 1부터 100까지 정수로 난수 발생
n=randint(1,5)
print(n)