num = int(input())
for i in range(num) :
    a = list(map(int,input().split()))
    print(f"You get {a[0]//a[1]} piece(s) and your dad gets {a[0]%a[1]} piece(s).")