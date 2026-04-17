import sys
from collections import deque


def main():
    print_ = print
    input = lambda:sys.stdin.readline().rstrip()

    n = int(input())
    for _ in range(n):
        data = input()
        left = deque()
        right = deque()
        for e in data:
            if e not in ["<", ">", "-"]:
                left.append(e)
                continue

            if e == "<" and left:
                right.appendleft(left.pop())
            elif e == ">" and right:
                left.append(right.popleft())
            elif e == "-" and left:
                left.pop()
        print_(*(left+right), sep="")

main()