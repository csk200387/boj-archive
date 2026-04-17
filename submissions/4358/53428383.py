import sys
dic = {}
sm = 0
for line in sys.stdin :
    if line != "\n" :
        sm += 1
        i = line.rstrip()
        try :
            dic[i] += 1
        except :
            dic[i] = 1
    else :
        break
for x,y in sorted(dic.items()) :
    y = 100*(y/sm)
    print(f"{x} {y:.4f}")