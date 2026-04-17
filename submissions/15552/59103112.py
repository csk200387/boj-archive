import sys
input=lambda:sys.stdin.readline().rstrip()
print=sys.stdout.write;
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(f"{a+b}\n")