student=[]
score=0
for i in range(5):
    score=int(input('학생%d'%(i+1)+' 점수 입력 : '))
    student.append(score)
    score+=score
avg=score/len(student)

print('총점 : %d'%score)
print('평균 : %.2f'%avg)