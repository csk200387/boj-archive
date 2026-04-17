import sys
input = lambda:sys.stdin.readline().rstrip()

def main():
    print_ = print
    size, line = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(line):
        a,b = map(int, input().split())
        print_(sum(arr[a-1:b]))
main()