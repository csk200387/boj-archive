import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
for i in range(n):
    word = input()
    if word[-1] == ".":
        print(word)
    else:
        print(word+".")