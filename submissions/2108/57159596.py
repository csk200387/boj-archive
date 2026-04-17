import sys
from collections import Counter
input = lambda:sys.stdin.readline().rstrip()

def mean() :
    r = sum(arr)/len(arr)
    print(round(r))

def median() :
    l = len(arr)
    if l == 1 :
        print(arr[0])
    elif l % 2 == 0 :
        t = l//2
        print(round((arr[t-1]+arr[t])/2))
    else :
        print(arr[int(l/2)])

def mode() :
    m = Counter(arr).most_common(2)
    if len(arr) > 1 :
        if m[0][1] == m[1][1]:
            print(m[1][0])
        else:
            print(m[0][0])
    else:
        print(m[0][0])

def rangee() :
    print(max(arr)-min(arr))


size = int(input())
arr = [int(input()) for _ in range(size)]
arr.sort()

mean()
median()
mode()
rangee()