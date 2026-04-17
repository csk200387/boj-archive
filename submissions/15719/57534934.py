sum = 0
n = int(input())
tmp = ""
st = input()
i = 0
while i < len(st) :
    j = i + 1
    while j < len(st) and st[j] != " " :
        j += 1
    sum += int(st[i:j])
    i = j + 1
gsum = n * (n + 1) // 2
print(n-gsum+sum)