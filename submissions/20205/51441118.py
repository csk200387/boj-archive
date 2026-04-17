n1, n2 = map(int, input().split(" "))
for _ in range(n1):
    inp = input().split(' ')
    for _ in range(n2):
        for i in inp:
            print(f"{i} " * n2, end="")
        print()