num = int(input())
a = []
for i in range(num):
    a.append(int(input()))
print("Junhee is not cute!" if a.count(1) < a.count(0) else "Junhee is cute!")