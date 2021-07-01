# 파티에 참석한 사람이 다음과 같을 때 집합 생성하고 그림과 같이 출력
# partyA : "Park", "Kim", "Lee"
# partyB : "Park", “길동“, “몽룡”

# 집합 생성
partyA={"Park","Kim","Lee"}
partyB={"Park","길동","몽룡"}

# 파티에 참석한 모든사람
print(partyA.union(partyB))
# 2개의 파티에 참석한 모든사람
print(partyA&partyB) # a.intersection(b)
# 파티 A에만 참석한 사람
print(partyA-partyB) # a.difference(b)
# 파티 B에만 참석한 사람
print(partyB-partyA)