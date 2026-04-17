def count_factors_zero(n):
    count = 0
    i = 5
    while (n / i >= 1):
        count += int(n / i)
        i *= 5
    return count

for i in range(int(input())) :
    n = int(input())
    print(count_factors_zero(n))