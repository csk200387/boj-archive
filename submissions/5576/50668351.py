W = []
K = []
for i in range(10) :
    a = int(input())
    W.append(a)
for i in range(10) :
    a = int(input())
    K.append(a)
W.sort(reverse=True)
K.sort(reverse=True)
print(sum(W[0:3]), sum(K[0:3]))