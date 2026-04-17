arr = [list(i.strip()) for i in open(0)]
length = len(arr[0])
for i in range(length):
    if arr[0][i] == '.' and arr[1][i] == 'o':
        arr[0][i] = 'o'
        arr[1][i] = 'w'
        arr[2][i] = 'l'
        arr[3][i] = 'n'
        arr[4][i] = '.'
    elif arr[0][i] == 'o':
        arr[0][i] = '.'
        arr[1][i] = 'o'
        arr[2][i] = 'm'
        arr[3][i] = 'l'
        arr[4][i] = 'n'
for i in arr:
    print(''.join(i))