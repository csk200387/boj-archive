import sys
input = lambda:sys.stdin.readline().rstrip()
ar = [0]*10001
for i in range(int(input())) :
    ar[int(input())-1] += 1
for i in range(10001) :
    if ar[i] > 0 :
        for _ in range(ar[i]) :
            print(i+1)