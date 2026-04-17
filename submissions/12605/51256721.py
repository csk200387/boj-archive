import sys
input = lambda:sys.stdin.readline().rstrip()
for i in range(0,int(input())) :
    print(f"Case #{i+1}:", " ".join(reversed(input().split())))