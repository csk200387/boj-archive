import sys
input = lambda:sys.stdin.readline().rstrip()
Test, sysTest = map(int,input().split())
count = 0
for i in range(Test+sysTest) :
    a,b = map(int,input().split())
    count += 1
    if a == b :
        res = "Accepted"
        break
    else :
        if count > sysTest and sysTest > 0 :
            res = "Why Wrong!!!"
            break
        else :
            res = "Wrong Answer"
            break
print(res)