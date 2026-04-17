a = input()
b = input()
arr=[0]
def check(ai, bi):
    c = 0
    while a[ai] == b[bi]:
        c += 1
        ai += 1
        bi += 1
    return c
ai = 0
bi = 0
i = 0
while True:
    try:
        if a[ai] ==b[bi]:
            arr.append(check(ai,bi))
        if i % 2 == 0:ai+=1
        else:bi+=1
        i += 1
    except IndexError:
        break
print(max(arr))