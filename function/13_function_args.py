# 가변길이 매개변수 : 1개의 매개변수로 개수가 정해지지않은
# 여러개의 값을 전달 받을 때 사용하는 매개변수
# 매개변수 형태 : *매개변수이름

def show_players(*players):
    print(players)
    print(type(players))
    for player in players:
        print(player,end='')
    print()
show_players('박지성')
show_players('손흥민','기성용')
show_players('박지성','손흥민','황의조')