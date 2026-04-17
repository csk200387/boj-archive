for i in range(int(input())):
 d=input()
 while d!="".join(sorted(d)):d=str(int(d)-1)
 print(f"Case #{i+1}: {d}")