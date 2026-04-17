import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
ar = deque([])
def push_front(n) :
    ar.appendleft(n)
def push_back(n) :
    ar.append(n)
def pop_front() :
    if len(ar) == 0 :
        print(-1)
    else :
        print(ar.popleft())
def pop_back() :
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
def front() :
    if len(ar) == 0 :
        print(-1)
    else :
        print(ar[0])
def back() :
    if len(ar) == 0 :
        print(-1)
    else :
        print(ar[-1])
if __name__ == "__main__" :
    for _ in range(int(input())) :
        tmp = input().split()
        if tmp[0] == "push_front" :
            push_front(int(tmp[1]))

        elif tmp[0] == "push_back" :
            push_back(int(tmp[1]))

        elif tmp[0] == "pop_front" :
            pop_front()

        elif tmp[0] == "pop_back" :
            pop_back()

        elif tmp[0] == "size" :
            size()

        elif tmp[0] == "empty" :
            empty()

        elif tmp[0] == "front" :
            front()
            
        else :
            back()