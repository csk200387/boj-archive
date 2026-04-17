num = int(input())
for i in range(num) :
    a = input().split()
    b = list(a[1])
    del b[int(a[0])-1]
    print("".join(b))