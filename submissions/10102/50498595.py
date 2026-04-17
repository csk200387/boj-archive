num = int(input())
f = input()
print("A" if f.count("B") < f.count("A") else "Tie" if f.count("B") == f.count("A") else "B")