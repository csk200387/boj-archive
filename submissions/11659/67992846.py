import sys
input = lambda:sys.stdin.readline().rstrip()
def main():
    print_ = print
    size, line = map(int, input().split())
    arr = list(map(int, input().split()))
    tmparr = [0]
    tmp = 0
    for i in arr:
        tmp += i
        tmparr += [tmp]
    for i in range(line):
        a, b = map(int, input().split())
        print(tmparr[b]-tmparr[a-1])
main()