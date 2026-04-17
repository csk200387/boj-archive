import sys
input = lambda:sys.stdin.readline().rstrip()
a, b, c = [0] * 3
for i in range(int(input())):
    T, con = input().split()
    if T == "section":
        a += 1
        print(f"{a}", con)
    if T == "subsection":
        b += 1
        print(f"{a}.{b}", con)
    if T == "subsubsection":
        c += 1
        print(f"{a}.{b}.{c}", con)