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