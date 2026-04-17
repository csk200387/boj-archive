def get_sum(st):
    sum = 0
    i = 0
    while i < len(st):
        j = i + 1
        while j < len(st) and st[j] != " ":
            j += 1
        sum += int(st[i:j])
        i = j + 1
    return sum

n = int(input())
st = input()
gsum = n * (n + 1) // 2
print(n - gsum + get_sum(st))