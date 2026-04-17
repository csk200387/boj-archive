for i in open(0):
 if i=="END\n":break
 else:print(i[-2::-1],end="")