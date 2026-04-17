from collections import deque
import sys

input = lambda:sys.stdin.readline().rstrip()
queue = deque([])
def push(n) :
    queue.append(n)

def pop() :
    if len(queue) == 0 :
        print(-1)
    else :
        print(queue.popleft())

def size() :
    print(len(queue))

def empty() :
    if len(queue) == 0 :
        print(1)
    else :
        print(0)

def front() :
    t = len(queue)
    if t == 0 :
        print(-1)
    else :
        print(queue[0])

def back() :
    t = len(queue)
    if t == 0 :
        print(-1)
    else :
        print(queue[len(queue)-1])
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
        elif tmp[0] == "front":
            front()
        else :
            back()