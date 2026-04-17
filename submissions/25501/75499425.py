import sys
input = lambda:sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

def is_palindrome(s, start, end, count=0):
    count += 1
    if start >= end:
        return 1, count    
    if s[start] == s[end]:
        return is_palindrome(s, start + 1, end - 1, count)
    else:
        return 0, count

n = int(input())
for i in range(n):
    data = input()
    result, count = is_palindrome(data, 0, len(data) - 1)
    print(result, count)