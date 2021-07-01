# 함수에 dict 전달하는 예제

# 함수 이름 : show_names(names)
# 함수 기능 : 전달받은 변수의 값을 반복문으로 활용해서 요소값으로 출력
# dict가 전달 된다고 가정
def show_info(info):
    # for name in info:
    print(info)
    print('이름 : '+info['name'])
    print('연락처 : ' +info['phone'])
# 함수 테스트
# 리스트를 인수로 전달한 후 출력확인
info_list={'name':'kim','age':23,'phone':'010-1234-1324'}
show_info(info_list)