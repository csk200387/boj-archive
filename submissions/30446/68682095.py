predata = [9, 9, 90, 90, 900, 900, 9000, 9000, 90000, 90000, 900000]

def is_palindrome(num):
    if num < 0:
        return False

    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return original_num == reversed_num

def oddpal(rng, n):
    cnt = 0
    for i in range(10**(rng-1), 10**rng):
        for center in range(10):
            number = str(i) + str(center) + str(i)[::-1]
            if int(number) > n:
                return cnt
            cnt += 1
    return cnt

def evenpal(rng, n):
    cnt = 0
    for i in range(10**(rng-1), 10**rng):
        number = str(i) + str(i)[::-1]
        if int(number) > n:
            return cnt
        cnt += 1
    return cnt

def main():
    n = int(input())

    length = len(str(n))
    cnt = 0
    if length % 2 == 0:
        cnt = evenpal(length//2, n)
    else:
        cnt = oddpal(length//2, n)

    print(cnt + sum(predata[:length-1]))

main()