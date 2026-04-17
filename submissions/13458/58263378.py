N = int(input())
arr = map(int, input().split())
B, C = map(int, input().split())
sum = 0
for i in arr :
    t = i - B
    sum += 1
    if t > 0 :
        if t % C == 0 :
            sum += t // C
        else :
            sum += t // C + 1
print(sum)