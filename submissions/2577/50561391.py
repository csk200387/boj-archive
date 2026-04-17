A = int(input())
B = int(input())
C = int(input())
sum = A*B*C
dic = {}
for i in range(10) :
    dic[str(i)] = 0
for i in str(sum) :
    dic[i] += 1
for i in dic.values() :
    print(i)