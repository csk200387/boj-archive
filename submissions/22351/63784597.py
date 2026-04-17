s = input()
right = 1
left = 1
while True:
    r = int(s[:right])
    l = int(s[-left:])
    t = "".join([str(i) for i in range(r,l+1)])
    if s == t:
        print(r, l)
        break
    
    if r > l:
        left += 1
    elif l < r:
        right += 1
    elif l == r:
        left += 1
    else:
        right += 1