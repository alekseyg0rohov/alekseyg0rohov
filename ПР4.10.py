a,b = int(input())
def f(a, b):
    if a <= 0 or b <= 0:
        return 0
    j, f = 0, 1
    s = 0
    for i in range(1, b + a):
        if i >= b:
            s += j
        j, f = f, j + f
    return s
r = f(a, b)
print(r)
