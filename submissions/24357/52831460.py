import sys

input = lambda:sys.stdin.readline().rstrip()

arr = [[]*3]*3

def p() :
    arr[l][m] += 1

for i in range(3) :
    arr[i] = list(map(int, input().split()))

for i in range(9) :
    l = i//3 # 행
    m = i%3  # 열
    if arr[l][m] != 9 :
        if i == 0 :
            if arr[l+1][m+1] == 9 :
                p()
            if arr[l+1][m] == 9 :
                p()
            if arr[l][m+1] == 9 :
                p()
        elif i == 1 :
            if arr[l][m-1] == 9 :
                p()
            if arr[l+1][m-1] == 9 :
                p()
            if arr[l][m+1] == 9 :
                p()
            if arr[l+1][m+1] == 9 :
                p()
            if arr[l+1][m] == 9 :
                p()
        elif i == 2 :
            if arr[l][m-1] == 9 :
                p()
            if arr[l+1][m] == 9 :
                p()
            if arr[l+1][m-1] == 9 :
                p()
        elif i == 3 :
            if arr[l-1][m] == 9 :
                p()
            if arr[l-1][m+1] == 9 :
                p()
            if arr[l][m+1] == 9 :
                p()
            if arr[l+1][m] == 9 :
                p()
            if arr[l+1][m+1] == 9 :
                p()
        elif i == 4 :
            if arr[l-1][m-1] == 9 :
                p()
            if arr[l-1][m] == 9 :
                p()
            if arr[l-1][m+1] == 9 :
                p()
            if arr[l][m-1] == 9 :
                p()
            if arr[l][m+1] == 9 :
                p()
            if arr[l+1][m-1] == 9 :
                p()
            if arr[l+1][m] == 9 :
                p()
            if arr[l+1][m+1] == 9 :
                p()
        elif i == 5 :
            if arr[l-1][m] == 9 :
                p()
            if arr[l-1][m-1] == 9 :
                p()
            if arr[l][m-1] == 9 :
                p()
            if arr[l+1][m-1] == 9 :
                p()
            if arr[l+1][m] == 9 :
                p()
        elif i == 6 :
            if arr[l-1][m] == 9 :
                p()
            if arr[l-1][m+1] == 9 :
                p()
            if arr[l][m+1] == 9 :
                p()
        elif i == 7 :
            if arr[l-1][m-1] == 9 :
                p()
            if arr[l-1][m] == 9 :
                p()
            if arr[l-1][m+1] == 9 :
                p()
            if arr[l][m-1] == 9 :
                p()
            if arr[l][m+1] == 9 :
                p()
        elif i == 8 :
            if arr[l-1][m-1] == 9 :
                p()
            if arr[l-1][m] == 9 :
                p()
            if arr[l][m-1] == 9 :
                p()

for i in range(3) :
    print(*arr[i])