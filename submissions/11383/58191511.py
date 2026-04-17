def double_char(s):
    return ''.join([c*2 for c in s])

n, m = map(int, input().split())
inp = []
arr = []
for i in range(n) :
    s = input()
    inp.append(double_char(s))
for i in range(n) :
    arr.append(input())
print("Eyfa" if inp == arr else "Not Eyfa")