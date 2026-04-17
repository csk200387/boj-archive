num = int(input())
count = 1
while True :
    count += 1
    if num % 2 == 0 :
        num = num//2
    else :
        num = (3 * num) + 1
    if num == 1 :
        print(count)
        break