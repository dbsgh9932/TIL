def order():
    price=int(input('상품가격 입력 : '))
    count=int(input('주문수량 입력 : '))

    print('------------------')
    print('상품가격 : %d원' % price)
    print('주문수량 : %d개'% count)
    return price * count

print('주문액 : ',order(),'원')

