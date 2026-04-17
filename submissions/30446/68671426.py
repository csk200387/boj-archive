#!/usr/bin/python3

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

def oddpal(rng, n):
    cnt = 0
    for i in range(10**(rng-1), 10**rng):
        if i > n:
            return cnt
        print(str(i) + str(i)[::-1])
        cnt += 1
    return cnt

def evenpal(rng, n):
    cnt = 0
    for i in range(10**(rng-1), 10**rng):
        if i > n:
            return cnt
        print(str(i) + str(i)[::-1])
        cnt += 1
    return cnt

n = int(input())

length = len(str(n))
cnt = 0
if length % 2 == 0:
    cnt = evenpal(length//2, n)
else:
    cnt = oddpal(length//2, n)
# for i in range(10**(length-1), n+1):
#     print(i)

print(cnt + sum(predata[:length-1]))