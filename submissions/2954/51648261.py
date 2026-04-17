ar = ["a", "e", "i", "o", "u"]
apr  = ["apa", "epe", "ipi", "opo", "upu"]
inp = input()
for i in range(5) :
    inp = inp.replace(apr[i], ar[i])
print(inp)