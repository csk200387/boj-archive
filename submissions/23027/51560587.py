inp = input()
if inp.count("A") != 0 :
    for i in ["B", "C", "D", "F"] :
        inp = inp.replace(i,"A")
    print(inp)
elif inp.count("B") != 0 :
    for i in ["C", "D", "F"] :
        inp = inp.replace(i,"B")
    print(inp)
elif inp.count("C") != 0 :
    for i in ["D", "F"] :
        inp = inp.replace(i,"C")
    print(inp)
else :
    print("A"*len(inp))