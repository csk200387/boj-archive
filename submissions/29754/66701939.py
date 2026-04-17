import sys
from collections import defaultdict
input = lambda:sys.stdin.readline().rstrip()

def return_time(start, end):
    start_hour, start_min = map(int, start.split(":"))
    end_hour, end_min = map(int, end.split(":"))
    return (end_hour - start_hour) * 60 + (end_min - start_min)

N, M = map(int, input().split())

data = defaultdict(list)

for _ in range(N):
    name, day, start_time, end_time = input().split()
    day = int(day)
    data[name].append((return_time(start_time, end_time)))

result = []
for i in data.keys():
    if len(data[i]) >= 5 and sum(data[i]) >= 3600:
        result.append(i)
result.sort()

if result:
    for i in result:
        print(i)
else:
    print(-1)