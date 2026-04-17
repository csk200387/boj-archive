import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
k = {
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
}

s = {input() for _ in range(n)}

if len(k & s) != n:
    print("YES")
else:
    print("NO")