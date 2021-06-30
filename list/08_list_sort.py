# sort() : 리스트 정렬, 원본 리스트 변경
scores=[90,78,81,64,89]
scores.sort() # 기본값 오름차순
print(scores)

scores=[90,78,81,64,89] ; print()
scores.sort(reverse=True) # 내림차순
print(scores)

scores=[90,78,81,64,89] ; print()
scores.reverse() # 원소 순서를 역순으로 (정렬x)
print(scores)

## 문자의 정렬 - 대문자<소문자,A~Z,a~z
char=['b','A','d','C'] ; print()
char.sort() # 오름차순
print(char)

char=['b','A','d','C'] ; print()
char.sort(reverse=True)
print(char) # 내림차순

# 대소문자 구별없이 정렬
# key=str.lower
char=['b','A','d','C'] ; print()
char.sort(key=str.lower)
print(char)

# 대소문자 구별없이 내림차순
char=['b','A','d','C'] ; print()
char.sort(key=str.lower,reverse=True)
print(char)

# 문자열은 첫 문자로 정렬됨
ids=['SKY','red','Blue','eBook','GREEN']
ids.sort() # 오름차순 정렬, 첫 문자 기준 정렬
print(ids)

# sorted() : 원본 유지하면서 정렬된 새로운 리스트 반환
a=[3,5,2,1,4]
b=sorted(a)
print('a :',a)
print('b :',b)