dictionary={}

while True:
    eng=input('\n영어 단어 등록 (종료는 quit) : ')

    if eng=='quit':
        break # 종료
    elif eng not in dictionary:
        kor=input('%s 뜻 입력 (종료는 quit) : '%eng)# 사전에 단어가 없는 경우 -> 뜻을 입력하시오
        dictionary[eng]=kor
    else:
        print('%s는 이미 등록된 단어입니다.'%eng)  # 사전에 단어가 있는 경우 -> 이미 등록된 단어입니다.

print(dictionary)

print('\n사전에서 단어를 검색하세요.')

while True:
    eng=input('검색 할 단어 입력 (종료는 quit) : ')

    if eng == 'quit':
        break  # 종료
    elif eng in dictionary: # 입력된 단어가 사전에 있는경우
        print('%s의 뜻은 %s 입니다'%(eng,dictionary[eng]))
    else:
        print('%s는 사전에 없는 단어입니다.'%eng)
print('\n 종료합니다.')