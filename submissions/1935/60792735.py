n = int(input())
inp = input()
lit = []
stack = []

for i in range(n):
    lit += [int(input())]


for i in inp :
    if i.isalpha():
        stack.append(lit[ord(i)-ord("A")])
    else :
        tmp2 = stack.pop()
        tmp1 = stack.pop()

        if i =="+" :
            stack.append(tmp1+tmp2)
        elif i == "-" :
            stack.append(tmp1-tmp2)
        elif i == "*" :
            stack.append(tmp1*tmp2)
        elif i == "/" :
            stack.append(tmp1/tmp2)

print(f"{stack[0]:.2f}")