import sys
input = lambda:int(sys.stdin.readline().rstrip())
print = sys.stdout.write
ar = [0]*10000
for i in range(input()) :
    ar[input()-1] += 1
for i in range(10000) :
    if ar[i] > 0 :
        for _ in range(ar[i]) :
            print(f"{i+1}\n")