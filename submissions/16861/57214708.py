num = int(input())
while True :
    t = sum(map(int, list(str(num))))
    if num % t == 0 :
        print(num)
        break
    else :
        num += 1