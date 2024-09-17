a, b = int(input()),int(input())
if a<b:
    print(2*a+2*b)
elif a>b:
    print(a-b+1)
elif a==b:
    print(b*b-b)
else:
    print("Ошибка")