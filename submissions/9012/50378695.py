from numba import jit

@jit(nopython=True)
def pro(a):
    while a.count('(') != 0 and a.count(')') != 0:
        a = a.replace("()","")
    print("YES" if len(a) == 0 else "NO")
num = int(input())
for i in range(0,num):
    a = input()
    pro(a)