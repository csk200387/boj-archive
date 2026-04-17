num = int(input())
dic = {}
for i in range(num) :
    a = input().split()
    dic[a[0]] = list(map(int,a[1:4]))
res = sorted(dic.items(), key=lambda x : (x[1][2], x[1][1], x[1][0]))

print(res[-1][0])
print(res[0][0])