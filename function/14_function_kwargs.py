# 가변길이 매개변수 **kwagrs - keyword arguments, key=value 형태로 값을 주고받음

def show_keywards(**kwargs):
    print(kwargs)
    print(type(kwargs))

show_keywards()
show_keywards(a=3)
show_keywards(id='sun',
              name='kim',
              phone='010-1234-1234'
              )
show_keywards(num=3,
              val='kim',
              str='abcdef')