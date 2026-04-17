a = int(input().split()[1])
ar = list(map(str,input().split()))
print(sorted(ar)[a-1])