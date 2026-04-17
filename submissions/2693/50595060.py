num = int(input())
for i in range(num) :
    a = sorted(list(map(int,input().split())))
    print(a[-3])