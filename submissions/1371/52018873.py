ar = [0]*26
while 1:
    try:
        line = input()
        for i in line.strip().replace(" ","") :
            t = ord(i)-97
            ar[t] += 1
    except EOFError:
        t = [i for i,v in enumerate(ar) if v == max(ar)]
        for l in t :
            print(chr(l+97), end="")
        break