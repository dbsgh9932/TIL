student=[]
score=0
good=0
num=int(input('학생 수 입력 : ')) # 학생 수 입력 후 학생 수 만큼 점수 입력

for i in range(num):
    scores=int(input('학생%d'%(i+1)+' 점수 입력 : '))
    student.append(scores)
    score+=scores
    if scores>=80:
        good+=1
avg=score/len(student)
print('총점 : %d'%score)
print('평균 : %.2f'%avg)
print('80점 이상 학생 %d명'%good)