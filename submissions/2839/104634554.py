n = int(input())
bag = 0
while 1:
    if n % 5 == 0 :
        bag += n//5
        break
    if n < 3:
        bag = -1
        break
    n -= 3
    bag += 1
print(bag)