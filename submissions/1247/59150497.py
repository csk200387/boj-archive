import sys
input = lambda:sys.stdin.readline().rstrip()
print = sys.stdout.write
for l in range(0,3):
    num = int(input())
    res = 0
    for i in range(num) :
        res += int(input())
    print("+" if res > 0 else "-" if res < 0 else "0")
    print("\n")