import sys
input = lambda:sys.stdin.readline().rstrip()

boardsize = int(input())
trycount = int(input())
board = [[*map(int, input().split())] for _ in range(boardsize)]

scoreList = []
damage = [*map(int, input().split())]

for i in range(trycount):
    score = 0
    for j in range(boardsize):
        if board[j][i] == 1:
            score += damage[j]
    scoreList.append(score)

print(max(scoreList))