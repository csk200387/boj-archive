def solution(n, q):
    tmp = ''
    n, q = int(n), int(q)
    while n > 0:
        n, mod = divmod(n, q)
        tmp += str(mod)
    return tmp[::-1] 

num, N = input().split()
bb = solution(num, N).split("0")
print(solution(sum(map(int,bb)), N))