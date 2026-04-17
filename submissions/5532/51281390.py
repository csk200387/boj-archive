import math
ar = []
for _ in range(5) :
    ar.append(int(input()))
a = math.ceil(ar[2]/ar[4])
b = math.ceil(ar[1]/ar[3])
print(ar[0] - a if a > b else ar[0] - b)