ar = [0]*1000000

for i in range(int(input())) :
    a = int(input())
    ar[a-1] += 1
for i in range(len(ar)) :
    if ar[i] > 0 :
        for _ in range(ar[i]) :
            print((i+1)%1000000)