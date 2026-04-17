import sys
input = lambda:sys.stdin.readline().rstrip()

class Node :
    def __init__(self, key) :
        self.key = key
        self.children = {}
        self.end = False
        
class Trie :
    def __init__(self) :
        self.root = Node(None)
        
    def insert(self, string) :
        cur = self.root
        for char in string :
            if char not in cur.children :
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.end = True
        
    def search(self, string) :
        cur = self.root
        for char in string :
            if char not in cur.children :
                return False
            cur = cur.children[char]
            if cur.end :
                return True
        return False
    
t = int(input())
for _ in range(t) :
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    arr.sort()
    trie = Trie()
    flag = False
    for i in arr :
        if trie.search(i) :
            flag = True
            break
        trie.insert(i)
    if flag :
        print("NO")
    else :
        print("YES")