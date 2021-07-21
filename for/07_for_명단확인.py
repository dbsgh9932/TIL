# 사용자가 입력한 이름이 명단에 있는지 검색 후 결과를 출력
# 입력양식
# 이름 입력 : 홍길동
# 출력양식
# 명단에 있습니다./없습니다.

namelist=['홍길동','이몽룡','성춘향','변학도']
#이름 입력
search_name=input('이름 입력 : ')

for name in namelist:
    if search_name==name: # 명단에서 이름을 찾은 경우 -> 반복중단
        find=True
        break # 찾은 경우 반복중단코드 사용
    else: # 명단에서 이름을 못찾은 경우 -> 찾을때 까지 반복
        find=False

# print(find)
if find: # if find==true 와 같음
    print('명단에 있습니다')
else:
    print('명단에 없습니다.')
