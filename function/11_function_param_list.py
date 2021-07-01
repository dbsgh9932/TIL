# 함수에 리스트 전달하는 예제

# 함수 이름 : show_names(names)
# 함수 기능 : 전달받은 변수의 값을 반복문으로 활용해서 요소값으로 출력
# 리스트가 전달 된다고 가정
def show_names(names):
    for name in names:
        print(name,end=' ')

# 함수 테스트
# 리스트를 인수로 전달한 후 출력확인
names_list=['kim','lee','park']
show_names(names_list)