import sys
input = lambda:sys.stdin.readline().rstrip()
total = int(input())
su = 0
for _ in range(9) :
    su += int(input())
print(total-su)