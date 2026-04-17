def main():
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    mx = 0
    for i in range(1, n + 1):
        cnt = 0
        for a, b in arr:
            if i in range(a, b + 1):
                cnt += 1
        if cnt == i:
            mx = i

    print(mx if mx else -1)

main()