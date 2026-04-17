import sys

while 1:
    line = sys.stdin.readline().rstrip()

    if line == "0":break
    print("num is", line)
    t = int(line)
    while 1:
        if t < 10:
            print(t)
            break
        t = sum(map(int, list(str(t))))