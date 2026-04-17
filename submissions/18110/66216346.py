import sys
input = lambda:sys.stdin.readline().rstrip()

def rnd(num):
    if num - int(num) >= 0.5:return int(num) + 1
    else:return int(num)
n = int(input())
if not n:
    print(0)
else:
    score = [int(input()) for _ in range(n)]
    tmp = rnd(n*0.15)
    t = sorted(score)[tmp:n-tmp]
    avg = rnd(sum(t)/len(t))
    print(avg)