product=[]

while True:
    new=input('상품 등록 (엔터키 누르면 종료) : ')
    product.append(new)
    if new=='':
        break
product=' '.join(product)
print('등록된 상품 : ',product)


item = []
while True :
    i = input("상품 등록 (엔터키 누르면 종료) : ")
    item.append(i)
    if i == "":
        break
item = " ".join(item)
print("등록된 상품 : ", item)