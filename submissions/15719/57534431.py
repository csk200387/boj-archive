sum = 0
n = int(input())
tmp = ""
gsum = n*(n+1)//2
for i in input() :
    if i != " " :
        tmp += i
    else :
        sum += int(tmp)
        tmp = ""
sum += int(tmp)
print(n-gsum+sum)