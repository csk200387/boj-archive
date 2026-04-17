import sys
input = lambda:sys.stdin.readline().rstrip()

while True:
    try:
        x = int(input())
        n = int(input())
        arr = [int(input()) for _ in range(n)]
        arr.sort()
        x *= 10000000
        start, end = 0, n-1
        r = (0, 0)
        while start < end:
            s = arr[start] + arr[end]
            if s == x:
                r = (arr[start], arr[end])
                break
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