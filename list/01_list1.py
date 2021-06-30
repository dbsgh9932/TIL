# 리스트 만들기
# 변수명=[값1,값2,..값n]
# 변수명=[] - 비어있는 리스트 생성

# 단일 자료형 list
ints=[1,2,3,4,5]
floats=[1.1,2.2,3.3,4.4,5.5]

# 복합 자료형 list
names=['이몽룡','성춘향','홍길동']

# 리스트 안에 리스트를 포함 할 수 있음
numbers=[100,200,300,[10,20,30]]

# 리스트 반환
# 리스트 명으로 접근
print(ints)
print(floats)
print(names)
print(numbers)

# 각 원소 접근
for name in names:
    print(name)
    print(type(name))

# 각 원소를 index를 통해 접근
for i in range(0,len(ints)):
    print(i) # 0 1 2 3 4
    print(ints[i]) # 1 2 3 4 5 (ints의 원소값을 출력)

# 인덱스를 통해 원소에 접근
print(numbers[3])

# 리스트 각각의 값을 변수에 저장
nums=[1,2,3]
# 리스트 nums의 원소값 각각을 a,b,c 변수에 저장하시오
                                         # a,b,c=nums[0],nums[1],nums[2]
                                           a,b,c=nums # 리스트 각각의 값을 차례대로 저장
print(nums)
print(a,b,c)

## 리스트 특징
# 원소의 갯수 = 변수의 갯수 여야한다
# ex) a,b=nums (nums=[1,2,3]) X
#     a,b,c=nums (nums=[1,2]) X