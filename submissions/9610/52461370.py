ar = [ [0,0], [0,0], 0 ]

for i in range(int(input())) :
    t = input()
    if t.count("0") == 0 :
        a, b = map(int, t.split())
        ar[(a>0)][(b>0)] += 1
    else :
        ar[2] += 1

print(f"Q1: {ar[1][1]}")
print(f"Q2: {ar[0][1]}")
print(f"Q3: {ar[0][0]}")
print(f"Q4: {ar[1][0]}")
print(f"AXIS: {ar[2]}")