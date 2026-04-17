import sys
input = lambda:sys.stdin.readline().rstrip()
s1 , s2 = map(int, input().split())
count = 0
for _ in range(s1+s2) :
    ans, user = map(int, input().split())
    if ans == user :
        count += 1
    else :
        print("Wrong Answer")
        exit()
if count == s1+s2 :
    print("Accepted")
else :
    print("Why Wrong!!!")