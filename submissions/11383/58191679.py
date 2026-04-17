def double_char(s):
    return ''.join([c*2 for c in s])
n, m = map(int, input().split())
inp = [double_char(input()) for _ in range(n)]
arr = [input() for _ in range(n)]
print("Eyfa" if inp == arr else "Not Eyfa")