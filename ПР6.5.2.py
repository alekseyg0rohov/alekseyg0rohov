numbers=[]
n=int(input())
for i in range(n):
    m=int(input())
    if m not in numbers:
        numbers.append(m)
print(*numbers, sep="\n") 