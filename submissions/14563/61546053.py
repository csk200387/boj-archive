input()
for num in map(int, input().split()):
    s = [i for i in range(1, num) if num % i == 0]
    if sum(s) == num:
        print("Perfect")
    elif sum(s) > num:
        print("Abundant")
    else:
        print("Deficient")