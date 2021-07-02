def order():
    price=int(input('상품 가격 입력 : '))
    qty=int(input('주문 수량 입력 : '))
    amount=price*qty

    if amount>=100000:
        discount=amount*0.1
    elif amount>=50000:
        discount=amount*0.05
    else:
        discount=0
    total=amount-discount
    print('--------------------')
    print('주문액 : %d원' % amount)
    print('할인액 : %d원' % discount)
    print('주문액 : %d원' % total)
order()
