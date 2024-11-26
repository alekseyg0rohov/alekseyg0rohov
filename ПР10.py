n=int(input())
matrix=[]
for i in range(n):
    matrix.append(input().split())
change=[int(i) for i in input().split()]
a,b=change[0],change[1]
for i in range(n):
    matrix[i][b],matrix[i][a]=matrix[i][a],matrix[i][b]
for hot in matrix:
    print(*hot)
file=open('Горохов Алексей Владимирович_УБ-42_vvod.txt','w')
file.write(str(matrix))
file.close()
file=open('Горохов Алексей Владимирович_УБ-42_vvod.txt')
b=file.read()
file2=open('Горохов Алексей Владимирович_УБ-42_vivod.txt','w')
file2.write(str(b))
file2.close()
file2=open('Горохов Алексей Владимирович_УБ-42_vivod.txt')
print(*file2)
file2.close()