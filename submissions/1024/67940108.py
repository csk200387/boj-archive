def main():
    N, L = map(int, input().split())
    for i in range(L, 101):
        f = N-i*(i+1)/2
        if f % i == 0:
            f = int(f/i)
            if f >= -1:
                print(*range(f+1, f+i+1))
                exit()
    print(-1)
main()