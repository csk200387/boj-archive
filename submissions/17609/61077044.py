import sys
input = lambda:sys.stdin.readline().rstrip()

def is_palindrome(s):
    return s == s[::-1]

def is_pseudo_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if is_palindrome(s[left+1:right+1]):
                return True
            if is_palindrome(s[left:right]):
                return True
            return False
        left += 1
        right -= 1

    return True

for i in range(int(input())) :
    t = input()
    if is_palindrome(t):
        print(0)
    elif is_pseudo_palindrome(t):
        print(1)
    else:
        print(2)