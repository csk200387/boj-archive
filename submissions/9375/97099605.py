import sys
input = lambda:sys.stdin.readline().rstrip()

testcase = int(input())

for _ in range(testcase):
    n = int(input())
    data = dict()
    for i in range(n):
        a, b = input().split()
        if data.get(b) == None:
            data[b] = [a]
        else:
            data[b].append(a)
    result = 1
    for key in data:
        result *= (len(data[key]))+1
    result -= 1
    print(result)