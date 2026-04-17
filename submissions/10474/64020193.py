from sys import stdin
while True:
    m, s = map(int, stdin.readline().split())
    if m == 0 and s == 0:
        break
    print(m // s, m % s, "/", s)