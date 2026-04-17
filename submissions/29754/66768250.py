import sys
import json
from collections import defaultdict
input = lambda:sys.stdin.readline().rstrip()

def return_time(start, end):
    start_hour, start_min = map(int, start.split(":"))
    end_hour, end_min = map(int, end.split(":"))
    return (end_hour - start_hour) * 60 + (end_min - start_min)

N, M = map(int, input().split())

data = defaultdict(lambda:defaultdict(list))

for _ in range(N):
    name, day, start_time, end_time = input().split()
    day = int(day)-1
    data[name][day//7].append((return_time(start_time, end_time)))
    # print(day//7)

result = []
for name in data.keys():
    is_ok = True
    for day in range(M//7):
        if len(data[name][day]) < 5 or sum(data[name][day]) < 3600:
            is_ok = False
            break
    if is_ok:
        result.append(name)

result.sort()

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

if result:
    for i in result:
        print(i)
else:
    print(-1)