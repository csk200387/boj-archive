import sys
from collections import defaultdict
input = lambda:sys.stdin.readline().rstrip()
dict = defaultdict(list)
for line in sys.stdin:
    data = line.rstrip()
    s_data = "".join(sorted(data))
    dict[s_data].append(data)
key_list = sorted(dict.keys(), key=lambda x: (-len(dict[x]), dict[x]))
for i in range(5):
    dict[key_list[i]].sort()
    joined = " ".join(dict[key_list[i]])
    print(f"Group of size {len(dict[key_list[i]])}: {joined} .")