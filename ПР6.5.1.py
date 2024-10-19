numbers=[]
for i in range(10):
    numbers.append(int(input()))
for i in range(len(numbers)-1):
    if numbers[i]<0 and numbers[i+1]<0:
        print(numbers[i],numbers[i+1])