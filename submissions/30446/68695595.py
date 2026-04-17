predata = [9, 9, 90, 90, 900, 900, 9000, 9000, 90000, 90000, 900000]

def oddpal(rng, n):
    cnt = 0
    for i in range(10**(rng-1), 10**rng):
        for center in range(10):
            nm = str(i) + str(center) + str(i)[::-1]
            if int(nm) > n:
                return cnt
            cnt += 1
    return cnt

def evenpal(rng, n):
    cnt = 0
    for i in range(10**(rng-1), 10**rng):
        nm = str(i) + str(i)[::-1]
        if int(nm) > n:
            return cnt
        cnt += 1
    return cnt

def main():
    n = int(input())
    if n < 10:
        print(n)
        exit()
    length = len(str(n))
    cnt = 0
    if length % 2 == 0:
        cnt = evenpal(length//2, n)
    else:
        cnt = oddpal(length//2, n)

    print(cnt + sum(predata[:length-1]))

main()