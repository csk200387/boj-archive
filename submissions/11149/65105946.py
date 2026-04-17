n = int(input())

for _ in range(n):
    data = input().split()
    result = []
    for i in data:
        aci = 0
        for j in range(len(i)):
            aci += (ord(i[j]) - 97) if i[j].isalpha() else 26
        result += [aci%27+97 if aci%27+97 != 123 else 32]
    print(*map(chr, result), sep='')