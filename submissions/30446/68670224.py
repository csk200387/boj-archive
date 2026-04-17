predata = [9, 9, 81, 90, 810, 900, 8100, 9000, 81000, 90000, 810000]

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

n = int(input())

length = len(str(n))
cnt = 0
for i in range(10**(length-1), n+1):
    if is_palindrome(i):
        cnt += 1

print(cnt + sum(predata[:length-1]))
