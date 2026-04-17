from collections import Counter
import sys
arr = []

while True :
    line = sys.stdin.readline().rstrip()
    if line == "***" :
        break
    else :
        arr.append(line)

counts = Counter(arr)

if len([k for k, v in counts.items() if v == max(counts.values())]) > 1:
    print("Runoff!")
else:
    print(max(counts, key=counts.get))