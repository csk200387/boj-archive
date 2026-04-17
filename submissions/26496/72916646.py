for i in open(0):
    line = i.strip()
    s = set()
    for x in range(len(line)):
        for y in range(x, len(line)):
            if (t:=line[x:y+1]) == t[::-1]:
                s.add(t)
    r = '" "'.join(sorted(s, key=lambda x:(len(x), line.index(x))))
    print(f'{len(s)} - "{r}"')