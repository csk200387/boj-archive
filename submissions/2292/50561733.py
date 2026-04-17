start = 1
num = int(input())
for i in range(1,10**10) :
    if num <= start :
        print(i)
        break
    else :
        start += i*6