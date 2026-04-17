import sys
input = lambda:sys.stdin.readline().rstrip()
s = set()
for i in range(int(input())) :
    ip = input()
    if ip == "all" :
        s = {t for t in range(1,21)}
    elif ip == "empty" :
        s = set()
    else :
        cmd, x = ip.split()
        x = int(x)
        if cmd == "add" :
            s.add(x)
        elif cmd == "remove" :
            s.discard(x)
        elif cmd == "check" :
            print(1 if x in s else 0)
        elif cmd == "toggle" :
            if x in s :
                s.discard(x)
            else :
                s.add(x)