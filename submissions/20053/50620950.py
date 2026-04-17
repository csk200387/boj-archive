num = int(input())
for i in range(num) :
    a = input()
    b = list(map(int,input().split()))
    print(min(b),max(b))