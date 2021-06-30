# 아래와 같은 데이터가 입력 됐을 때 숫자만 추출해서 총 합계를 구하시오

str_data="{a1:20},{a2:30},{a3:15},\
        {a4:50},{a5:-14},{a6:15},\
        {a7:20},{a8:70},{a9:-100}"

# 데이터 분리할 구분자 결정
split_str_data=str_data.split(',')
print(split_str_data)
print(split_str_data[0].split(':')[1].split('}')[0]) # {a1:20}를 선택해서 :기준으로 a1,20쪼개서 1번자리 '20}'을 뽑고
                                                     # }기준으로 20과 공백을 쪼갠 후 0번자리 20을 뽑아냄
# 반복문으로 각각의 숫자 분리
total=0
for i in range(0,len(split_str_data)):
    temp=split_str_data[i].split(':')[1].split('}')[0] # 추출값 모음
    total+=int(temp)
print('추출된 값의 합은',total,'입니다.')

