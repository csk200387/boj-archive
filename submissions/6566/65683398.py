D = {}
for d in [*open(0)]:
    l = d.rstrip()
    s = "".join(sorted(l))
    if s not in D:D[s]=[l]
    else:D[s]+=[l]
for i in sorted(D.keys(), key=lambda x: (-len(D[x]), D[x]))[:5]:
    print(f"Group of size {len(D[i])}: {' '.join(sorted(set(D[i])))} .")