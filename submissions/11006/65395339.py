n = int(input())
for i in range(n):
    legs, body = map(int, input().split())
    count = 0
    while legs != body:
        legs -= 2
        body -= 1
        count += 1
    print(body, count)