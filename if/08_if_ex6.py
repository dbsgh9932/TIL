print('''*********상품정보**********
1 노트북 : 1,200,000 원
2 디지털카메라 : 400,000 원
**************************''')
a=int(input('상품 번호 입력 : '))
if a==1 or a==2:
    b=int(input('주문 수량 입력 : '))
    print('*********주문내용**********')
    if a==1:
        x=b*1200000
        print('상품명 :    노트북')
        print('가격 :      %s 원'%format(x,','))
        print('주문 수량 :  %d'%b)
        print('주문액 :    %s 원'%format(x,','))
        if x >= 1000000:
            print('할인액 :    %s 원' % format(int(x * 0.1), ','))
            print('총 지불액 :  %s 원' % format(int(x - 0.1 * x), ','))
        else:
            print('할인액 :             0 원')
            print('총 지불액 :  %s 원'%format(x,','))
    else:
        x=b*400000
        print('상품명 : 디지털카메라')
        print('가격 :      %s 원'%format(x,','))
        print('주문 수량 :  %d'%b)
        print('주문액 :    %s 원'%format(x,','))
        if x >= 1000000:
            print('할인액 :    %s 원' % format(int(x * 0.1), ','))
            print('총 지불액 :  %s 원' % format(int(x - 0.1 * x), ','))
        elif x >= 500000:
            print('할인액 :    %s 원' % format(int(x * 0.05), ','))
            print('총 지불액 :  %s 원' % format(int(x - 0.05 * x), ','))
        else:
            print('할인액 :         0 원')
            print('총 지불액 :  %s 원' % format(x, ','))
else:
    print('잘못 입력하였습니다. 종료합니다.')