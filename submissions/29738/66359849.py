import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())

for i in range(n):
    score = int(input())

    if score <= 25:
        print(f"Case #{i+1}: World Finals")
    elif score <= 1000:
        print(f"Case #{i+1}: Round 3")
    elif score <= 4500:
        print(f"Case #{i+1}: Round 2")
    else:
        print(f"Case #{i+1}: Round 1")