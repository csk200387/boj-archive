import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == "0":break
    bed,cus = line.split()
    now = set()
    g = set()
    for c in cus:
        if c in g:
            continue
        if c in now:
            now.remove(c)
        elif len(now) == int(bed):
            g.add(c)
        else:
            now.add(c)
    if len(g) == 0:
        print("All customers tanned successfully.")
    else:
        print(f"{len(g)} customer(s) walked away.")