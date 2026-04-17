import sys
input = sys.stdin.readline

arr1 = []
arr2 = []

n = int(input().split()[0])
for i in range(n) :
    arr1.append(list(map(int,input().rstrip().split())))
    
n = int(input().split()[0])
for i in range(n) :
    arr2.append(list(map(int,input().rstrip().split())))
    
for i in range(len(arr1)) :
    a = []
    for h in range(len(arr2[0])) :
        tmp = 0
        for l in range(len(arr2)) :
            tmp += arr1[i][l]*arr2[l][h]
        a.append(tmp)
    print(" ".join(list(map(str,a))))