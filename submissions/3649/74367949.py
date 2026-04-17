import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
        n = int(input())
        arr = sorted(int(input()) for i in range(n))
        x *= 10000000
        start, end = 0, n-1
        r = (0, 0)
        while start < end:
            s = arr[start] + arr[end]
            if s == x:
                if abs(r[0]-r[1]) < abs(arr[start]-arr[end]):
                    r = (arr[start], arr[end])
            if s > x:
                end -= 1
            else:
                start += 1

        if r[0] == r[1] == 0:
            print('danger')
        else:
            print('yes', *sorted(r))
    except:
        break