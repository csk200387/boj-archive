import sys
input = lambda:sys.stdin.readline().rstrip()

class queue :

    def __init__(self) :
        """큐 생성자"""
        self.ar = []

    def push(self, n) :
        """큐에 n을 넣는다."""
        self.ar.append(n)

    def pop(self) :
        """큐에서 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다."""
        if len(self.ar) == 0 :
            print(-1)
        else :
            print(self.ar.pop(0))

    def size(self) :
        """큐에 들어있는 정수의 개수를 출력한다."""
        print(len(self.ar))

    def empty(self) :
        """큐가 비어있으면 1, 아니면 0을 출력한다."""
        if len(self.ar) == 0 :
            print(1)
        else :
            print(0)

    def front(self) :
        """큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다."""
        t = len(self.ar)
        if t == 0 :
            print(-1)
        else :
            print(self.ar[0])

    def back(self) :
        """큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다."""
        t = len(self.ar)
        if t == 0 :
            print(-1)
        else :
            print(self.ar[len(self.ar)-1])

queue = queue() #큐 생성

if __name__ == "__main__" :
    for _ in range(int(input())) :
        tmp = input().split()
        if tmp[0] == "push" :
            queue.push(int(tmp[1]))
        elif tmp[0] == "pop" :
            queue.pop()
        elif tmp[0] == "size" :
            queue.size()
        elif tmp[0] == "empty" :
            queue.empty()
        elif tmp[0] == "front":
            queue.front()
        else :
            queue.back()