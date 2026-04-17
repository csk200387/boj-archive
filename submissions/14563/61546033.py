input()
for num in map(int, input().split()):
    s = []
    for i in range(1, num):
        if num % i == 0:
            s.append(i)
    if sum(s) == num:
        print("Perfect")
    elif sum(s) > num:
        print("Abundant")
    else:
        print("Deficient")