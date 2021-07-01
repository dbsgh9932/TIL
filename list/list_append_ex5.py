product=[]
while True:
    new=input('상품 등록 (엔터키 누르면 종료) : ')
    if new=='':
        break
    product.append(new)

print('등록된 상품 : ',product)

for products in product:
    print('등록된 상품 : ',products,end=' ')