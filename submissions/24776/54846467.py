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
most_common = counter.most_common()
if most_common[0][1] == most_common[1][1]:
    print("Runoff!")
else:
    print(most_common[0][0])