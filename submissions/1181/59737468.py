r=[*{input()for _ in range(int(input()))}]
r.sort();r.sort(key=len)
print(*r,sep="\n")