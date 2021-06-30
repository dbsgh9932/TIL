student=[]
score=0
good=0
for i in range(5):
    scores=int(input('학생%d'%(i+1)+' 점수 입력 : '))
    student.append(scores)
    score+=scores
    avg=score/len(student)
    if scores>=80:
        good+=1

print('총점 : %d'%score)
print('평균 : %.2f'%avg)
print('80점 이상 학생 %d명'%good)