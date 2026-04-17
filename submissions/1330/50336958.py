num = input("").split(" ")
A = int(num[0])
B = int(num[1])
print("{}".format("==" if A == B else ">" if A > B else "<"))