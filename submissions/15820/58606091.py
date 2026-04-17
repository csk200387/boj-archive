import sys
input = lambda:sys.stdin.readline().rstrip()
s1 , s2 = map(int, input().split())
count = 0
for _ in range(s1) :
    ans, user = map(int, input().split())
    if ans != user :
        print("Wrong Answer")
        exit()
for _ in range(s2) :
    ans, user = map(int, input().split())
    if ans != user :
        print("Why Wrong!!!")
        exit()
print("Accepted")