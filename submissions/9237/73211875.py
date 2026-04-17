n = int(input())
arr = sorted(map(int, input()), reverse=1)
print(max(map(lambda x:arr.index(x)+1,arr)))