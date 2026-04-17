import sys
input = lambda:sys.stdin.readline().rstrip()
ar = []
def push(n) :
    ar.append(n)
def pop() :
    if len(ar) == 0 :
        print(-1)
    else :
        print(ar.pop())
def size() :
    print(len(ar))
def empty() :
    if len(ar) == 0 :
        print(1)
    else :
        print(0)
def top() :
    t = len(ar)
    if t == 0 :
        print(-1)
    else :
        print(ar[len(ar)-1])

if __name__ == "__main__" :
    for _ in range(int(input())) :
        tmp = input().split()
        if tmp[0] == "push" :
            push(int(tmp[1]))
        elif tmp[0] == "pop" :
            pop()
        elif tmp[0] == "size" :
            size()
        elif tmp[0] == "empty" :
            empty()
        else :
            top()