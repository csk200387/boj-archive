n = int(input())
arr = [*map(int, input().split())]
arr.sort(reverse=True)
while len(arr) > 1:
    if sum(arr) % 2 == 0:
        break
    arr.pop()

print(sum(arr) if sum(arr) % 2 == 0 else 0)