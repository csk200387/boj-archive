from collections import deque

counter, customer = map(int, input().split())
customers = deque(map(int, input().split()))

check = [customers.popleft() for _ in range(counter)]
result = [i+1 for i in range(counter)]
while customers:
    customer = customers.popleft()
    check = list(map(lambda x:x-min(check), check))
    result.append(check.index(0)+1)
    check[check.index(0)] = customer
print(result)