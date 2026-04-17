import random
arr = []
for _ in range(9) :
    arr.append(int(input()))
while True :
    random.shuffle(arr)
    if sum(arr[:7]) == 100 :
        print(*sorted(arr[:7]), sep="\n")
        break