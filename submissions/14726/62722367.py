import sys
input = lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())):
    cardnum = list(map(int, list(input())))
    for i in range(16):
        if i%2 == 0:
            cardnum[i] *= 2
            if cardnum[i] >= 10:
                cardnum[i] = cardnum[i]//10 + cardnum[i]%10
    if sum(cardnum)%10 == 0:
        print('T')
    else:
        print('F')