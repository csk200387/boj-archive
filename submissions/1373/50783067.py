import sys
input = sys.stdin.readline
print(oct(int("0b"+input().rstrip(), 2))[2::])