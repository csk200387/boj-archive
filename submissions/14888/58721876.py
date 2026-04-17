from itertools import permutations

n = int(input())

arr = [*map(int, input().split())]

t = input().split()
farr = []
tmp = ["+", "-", "*", "/"]
for index, l in enumerate(t) :
    for i in range(int(l)) :
        farr.append(tmp[index])

mx = 0
mn = 0
for c in permutations(farr, len(farr)) :
    result = arr[0]
    frin = 0
    for i in range(1, len(arr)) :

        if c[frin] == "+" :
            result += arr[i]

        elif c[frin] == "-" :
            result -= arr[i]

        elif c[frin] == "*" :
            result *= arr[i]

        else :
            result = int(result/arr[i])

        frin += 1

    print(result)
    if result > mx :
        mx = result
    if result < mn :
        mn = result

print(mx)
print(mn)