import sys
input = lambda:sys.stdin.readline().rstrip()

def ratToGrad(grad) :
    arr = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", 0, "F"]
    return 4.5 - arr.index(grad)*0.5

sum = 0
ratsum = 0

for i in range(20) :
    sub, rat, grad = input().split()
    if grad != "P" :
        sum += float(rat)*ratToGrad(grad)
        ratsum += float(rat)

print(round(sum/ratsum, 6))