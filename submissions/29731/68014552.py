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

for _ in range(n):
    t = input()

    if t not in k:
        print("Yes")
        exit(0)

print("No")