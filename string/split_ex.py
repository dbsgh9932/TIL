birth=input('생일 입력 (연/월/일) : ')
birth_split=birth.split('/')

print('당신은',birth_split[0],'년에 태어났고','\t')
print('생일은',birth_split[1],'월',birth_split[2],'일 이군요')