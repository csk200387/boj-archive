import re
def solution(n, q):
    tmp = ''
    n, q = int(n), int(q)
    while n > 0:
        n, mod = divmod(n, q)
        tmp += str(mod)
    return tmp[::-1] 

num, N = input().split()
sol = solution(num, N)
bb = filter(None, re.split("0{1,}",sol))
print(solution(sum(map(int,bb)), N))