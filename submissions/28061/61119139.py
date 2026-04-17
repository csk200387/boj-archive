n = int(input())
arr = map(int, input().split())
tmp = [c-n+i for i,c in enumerate(arr)]
print(max(tmp))