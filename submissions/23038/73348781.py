n, m = map(int, input().split())
arr = [[*input()] for _ in range(n*3)]
for x in range(n):
    for y in range(n):
        if arr[1+x*3][1+y*3] == '.':
            try:
                if arr[1+x*3][1+y*3+2] == '#':
                    arr[1+x*3][1+y*3+1] = '#'
                    arr[1+x*3][1+y*3] = '#'
            except IndexError:
                pass
            try:
                if arr[1+x*3+2][1+y*3] == '#':
                    arr[1+x*3+1][1+y*3] = '#'
                    arr[1+x*3][1+y*3] = '#'
            except IndexError:
                pass
            try:
                if arr[1+x*3-2][1+y*3] == '#':
                    arr[1+x*3-1][1+y*3] = '#'
                    arr[1+x*3][1+y*3] = '#'
            except IndexError:
                pass
            try:
                if arr[1+x*3][1+y*3-2] == '#':
                    arr[1+x*3][1+y*3-1] = '#'
                    arr[1+x*3][1+y*3] = '#'
            except IndexError:
                pass

for i in arr:
    print(*i, sep='')