import sys
input = lambda:sys.stdin.readline().rstrip()

def is_palindrome(s):
    return s == s[::-1]

def is_pseudo_palindrome(s):
    for i in range(len(s)):
        if is_palindrome(s[:i] + s[i + 1:]):
            return True
    return False

for i in range(int(input())) :
    t = input()
    if is_palindrome(t):
        print(0)
    elif is_pseudo_palindrome(t):
        print(1)
    else:
        print(2)