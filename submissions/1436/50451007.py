a = int(input())
b = 666
c = 0
while True:
    if str(b).find("666") != -1 :
        c += 1
        if c == a:
            print(b)
            break
        
    b += 1