a = int(input(""))
result = []
for i in range(0,a):
    result.append(input())
print("\n".join(sorted(list(map(str,result)))))