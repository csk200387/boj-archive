x,y=zip(*[[*map(int,i.split())] for i in [*open(0)][1::]])
print((max(x)-min(x))*(max(y)-min(y)))