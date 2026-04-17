import sys
s = set()
for _ in  range(15):
    s.update(sys.stdin.readline().rstrip().split())
print("chunbae" if "w" in s else "nabi" if "b" in s else "yeongcheol")