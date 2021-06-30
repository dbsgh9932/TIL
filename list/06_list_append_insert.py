# append() - 리스트의 끝에 새로운 요소 추가 / 리스트.append(새로 추가할 요소)
a=[1,2,3,4]
a.append(5) # a
print(a)
a.append([6,7])
print(a)

# a.append(8,9) # 2개 이상 원소 불가
# print(a) # TypeError: list.append() takes exactly one argument (2 given)

# 빈 리스트를 생성하고 요소 나중에 추가
values=[]
values.append(10)
values.append(20)
values.append(30)
print(values)

# 사용자에게 5개의 값을 입력받아서 리스트에 저장하는 코드
scores=[]
for i in range(5):
    num=int(input('값을 입력하세요 : '))
    scores.append(num)
    print(i+1,'번째 결과',scores)
print(scores)

# 위 코드에서 입력받은 값을 각 요소로 출력하는 코드를 작성하시오.
# 리스트 요소 출력
for j in range(len(scores)):
    print(scores[j])

# insert(위치,값) : 리스트 특정 위치에 요소 삽입
nums=[1,2,3,4,5]
nums.insert(1,200) # 1은 1번 인덱스(2번째) 자리를 의미
print(nums) # 2번째 자리에 200이 들어가고 나머지는 뒤로 밀림 -> [1,200,2,3,4,5]

nums.insert(-1,"홍길동") # 마지막 원소에 들어갔는데 마지막 자리의 5가 뒤로 밀려서
print(nums) # [1,200,2,3,4,홍길동,5] 라는 결과가 나옴

# insert로 맨 뒤에 삽입
nums.insert(len(nums),12.3) # 맨 뒤에 삽입은 길이를 선언 후 사용 -> 일반적으로 append()씀
print(nums)

nums.insert(len(nums)-1,[10,20])
print(nums)