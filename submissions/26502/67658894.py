import sys
input = lambda:sys.stdin.readline().rstrip()
data = {"y":"a","a":"e","e":"i","i":"o","o":"u","u":"y","Y":"A","A":"E","E":"I","I":"O","O":"U","U":"Y"}
def main():
    n = int(input())
    for _ in range(n):
        s = input()
        ans = ""
        for c in s:
            if c in data:ans += data[c]
            else:ans += c
        print(ans)

main()