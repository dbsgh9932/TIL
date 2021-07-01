dictionary={}

for i in dictionary:
    word=input('영어 단어 등록 (종료는 quit) : ')
    dictionary[word]='word'
    mean=input(word+'의 뜻 입력 (종료는 quit) : ')
    dictionary[mean]='mean'

print(dictionary)