ar = [0]*10000
for i in [*open(0)][1::] :
    ar[int(i)-1] += 1
for i in range(10000) :
    if ar[i] > 0 :
        for _ in range(ar[i]) :
            print(i+1)