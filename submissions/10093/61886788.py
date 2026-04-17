a,b = map(int, input().split())
arr = [str(i) for i in range(a+1, b)]
print(len(arr))
print(' '.join(arr))