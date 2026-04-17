v = input()
a = list(map(int,input().split()))
if sorted(a)[-1] % 2 == 0 :
    print(2*sorted(a)[-1])
else :
    print(3*sorted(a)[-1])