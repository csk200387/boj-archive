num = int(input())
a = 0
for i in range(1, num+1) :
    if num % i == 0 :
        a += i
print((a*5)-24)