def get_count(num_digits) :
    count = 0
    for i in range(1, num_digits + 1) :
        count += 9 * (10 ** (i - 1)) * i
    return count

def get_kth_digit(k) :
    num_digits = 1
    while True:
        count = get_count(num_digits)
        if k <= count :
            start = 10 ** (num_digits - 1)
            num = start + (k - 1) // num_digits
            digit = str(num)[(k - 1) % num_digits]
            return int(digit)
        k -= count
        num_digits += 1

_, k = map(int, input().split())
digit = get_kth_digit(k)
print(digit)