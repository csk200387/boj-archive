n = int(input())
bag = 0

while True :
    if n % 5 == 0 :
        bag += n//5
        break
    if n < 3:
        bag = -1
        break
    n -= 3
    bag += 1
# 3을 먼저 계산
print(bag)