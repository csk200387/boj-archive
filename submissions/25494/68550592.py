for _ in range(int(input())):
    cnt = 0
    A, B, C = map(int, input().split())
    for a in range(1, A+1):
        for b in range(1, B+1):
            for c in range(1, C+1):
                if a%b == b%c == c%a:
                    cnt += 1
    print(cnt)