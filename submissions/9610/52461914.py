ar = [ [0,0], [0,0], 0 ]
for i in range(int(input())) :
    a, b = map(int, input().split())
    if a and b :
        ar[(a>0)][(b>0)] += 1
    else :
        ar[2] += 1
print("Q1:", ar[1][1])
print("Q2:", ar[0][1])
print("Q3:", ar[0][0])
print("Q4:", ar[1][0])
print("AXIS:", ar[2])