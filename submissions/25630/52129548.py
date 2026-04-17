t = input()
a = input()
count = 0
for i in range(0,len(a)//2) :
    if a[i] != a[-i-1] :
        count += 1
print(count)