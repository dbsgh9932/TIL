#현금이 5000원 있고 사탕 가격이 120원이면 최대한 살 수있는 사탕의 갯수와
#사고 남은 돈은 얼마인가
cash=5000
candy=120
maxcandies=cash//candy
remainder=cash%candy
print('사탕 %d개를 사고 남은 돈 %d원'%(maxcandies,remainder))

