n = int(input())
for i in range(n,0,-1) :
    if len(str(i).replace("4","").replace("7","")) == 0:
        print(i)
        break