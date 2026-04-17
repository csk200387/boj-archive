import sys
input = lambda:sys.stdin.readline().rstrip()

input()
cards = list(map(int, input().split()))
input()
nums = list(map(int, input().split()))

dict = {}
for _ in range(len(cards)):
    tmp = cards.pop()
    if tmp in dict:
        dict[tmp] += 1
    else:
        dict[tmp] = 1
print(dict)
for num in nums:
    if num in dict:
        print(dict[num], end=' ')
    else:
        print(0, end=' ')