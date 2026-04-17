import sys
input = lambda:sys.stdin.readline().rstrip()

u, n = map(int, input().split())
p_list = [int(u)+1 for _ in range(u+1)]
nm_list = [None for _ in range(u+1)]
for i in range(n):
    nm, p = input().split()
    ip = int(p)
    if p_list[ip] == u+1:
        p_list[ip] = 1
    else:
        p_list[ip] += 1
    if not nm_list[ip]:
        nm_list[ip] = nm

index_m = p_list.index(min(p_list))
print(nm_list[index_m], index_m)