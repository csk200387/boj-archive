import sys
input = lambda:sys.stdin.readline().rstrip()

def main():
    print_ = print
    dic = {}
    
    n, m = map(int, input().split())
    
    for i in range(n):
        word = input()
        if len(word) < m:
            continue
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    
    arr = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]),x[0]))
    
    for i in arr:
        print_(i[0])

main()