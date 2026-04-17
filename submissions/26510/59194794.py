for i in map(int, input().split()) :
    for l in range(i) :
        r = " "*l+"*"+" "*((i-l-1)*2-1)+"*"
        if l == i-1 :
            r = " "*l+"*"
        print(r)