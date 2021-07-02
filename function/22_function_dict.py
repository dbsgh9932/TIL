students=[
    {'name':'홍길동','korean':'87','math':'98','english':'88','science':'95'},
    {'name': '이몽룡', 'korean': '92', 'math': '98', 'english': '96', 'science': '98'},
    {'name': '성춘향', 'korean': '76', 'math': '96', 'english': '94', 'science': '90'},
    {'name': '변학도', 'korean': '98', 'math': '92', 'english': '96', 'science': '92'},
    {'name': '박지성', 'korean': '95', 'math': '98', 'english': '98', 'science': '98'},
    {'name': '류현진', 'korean': '64', 'math': '88', 'english': '92', 'science': '92'}
]

# dict을 전달받아서 일부만 추출 후 재구성 - 반환하는 함수
def get_student_subinfo(stds):

    name=stds['name']
    korean=stds['korean']

    return {'name':name,'korean':korean}

# 반환된 name과 korean만 포함된 dict을 받아서 리스트 std_sublist에 추가
std_sublist=[]
for s in students:
    stds=get_student_subinfo(s)
    std_sublist.append(stds)

print(std_sublist)