n=int(input())
matrix=[]
for i in range(n):
    matrix.append(input().split())

change=[int(i) for i in input().split()]
file=open('Горохов Алексей Владимирович_УБ-42_vvod.txt','w')
file.write(str(n))
file.write(str(matrix))
file.write(str(change))
file.close()
a,b=change[0],change[1]

for i in range(n):
    matrix[i][b],matrix[i][a]=matrix[i][a],matrix[i][b]
for hot in matrix:
    print(*hot)


for hot in matrix:
    file2=open('Горохов Алексей Владимирович_УБ-42_vivod.txt','w')
    file2.write(str(matrix))
    file2.close()
    file2=open('Горохов Алексей Владимирович_УБ-42_vivod.txt')
    print(*file2)
    file2.close()