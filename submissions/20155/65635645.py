input()
from collections import Counter
cnt = Counter(input().split())
print(cnt.most_common()[0][0])