arr = list(map(int, input().split()))
t = ["A", "B", "C"]
c = arr.count
if c(0) == 3 or c(1) == 3 :
    print("*")
elif c(0) > c(1) :
    print(t[arr.index(1)])
else :
    print(t[arr.index(0)])