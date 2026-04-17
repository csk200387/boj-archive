a, *arr = open(0)
t = sorted(arr)
if t == arr :
    print("INCREASING")
elif t[::-1] == arr :
    print("DECREASING")
else :
    print("NEITHER")