n = int(input())
arr = [(0,0)]
cnt = 2
x, y = 0, 0
for i in range(35):
    cnt = i*2
    for t in range(cnt):
        if (cnt//2)%2 == 1:
            if t < cnt//2:
                y += 1
            else:
                x += 1
        else:
            if t < cnt//2:
                y -= 1
            else:
                x -= 1
        arr.append((x,y))
print(*arr[n])