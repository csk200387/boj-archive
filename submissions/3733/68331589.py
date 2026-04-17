for line in open(0):
    n, s = map(int, line.split())
    print(int(s//(n+1)))