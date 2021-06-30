#사용자로부터 점수를 입력받아서 학점을 구하는 프로그램
num=eval(input('점수 입력 : '))

if num>=90:
    print('학점은 A')
elif num>=80:
    print('학점은 B')
elif num>=70:
    print('학점은 C')
elif num>=60:
    print('학점은 D')
else:
    print('낙제')
