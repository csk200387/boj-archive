input()
for i in list(map(int, input().split())) :
    print(1 if i == int(i**0.5)**2 else 0, end=" ")