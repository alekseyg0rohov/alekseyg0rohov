n=int(input())
k=int(input())
m=int(input())
a = []
for i in range(1, n+1):
    a.append(i)
b = []
for i in range(1, k+1):
    b.append(i)
c = []
for i in range(1, m+1):
    c.append(i)
def pr(a):
    s = 1
    for i in range(len(a)):
        s *= a[i]
    return s
def sa(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s//len(a) 
print(a, b, c)
print(pr(a), pr(b), pr(c))
print(sa(a), sa(b), sa(c))