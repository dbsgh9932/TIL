student=[]
score=0
good=0
for i in range(5):
    scores=int(input('학생%d'%(i+1)+' 점수 입력 : '))
    student.append(scores)
    score+=scores
    if scores>=80:
        good+=1
avg=score/len(student)
print('총점 : %d'%score)
print('평균 : %.2f'%avg)
print('80점 이상 학생 %d명'%good)

# scores 정렬
student.sort(reverse=True)
print(student) # 입력한 점수 내림차순