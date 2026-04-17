import sys
input = lambda:sys.stdin.readline().rstrip()

n, *arr = open(0)
data = """Case #1: Round 1
Case #2: Round 2
Case #3: Round 3
Case #4: World Finals"""

print(*data.split("\n")[:int(n)], sep="\n")