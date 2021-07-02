# 리스트를 함수에 인수로 전달할 때

def show_list(func_list):
    func_list[0]=10 # 원본 my_list도 변경됨
    print(func_list)

    func_list=[10,20,30,40] # 새로운 변수생성 - 주소도 달라짐
    print(func_list)

my_list=[1,2,3,4]
show_list(my_list)
print(my_list)