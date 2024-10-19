numbers=[]
for i in range(10):
    numbers.append(int(input()))
mx=max(numbers)
mn=min(numbers)
for i in range(len(numbers)):
    if numbers[i]==mx:
        numbers[i]=mn
    elif numbers[i]==mn:
        numbers[i]=mx
print(numbers)
    
    