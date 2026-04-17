arr = [1]
for i in range(2, 46):
    arr.append(arr[-1]+i)
def sol(n):
    for a in arr:
        for b in arr:
            for c in arr:
                if n == a+b+c:
                    return True
    return False
for line in range(int(input())):
    print(int(sol(int(input()))))