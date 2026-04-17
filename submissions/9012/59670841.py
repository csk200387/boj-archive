for i in range(0,int(input())):
 a=input()
 while"()"in a:a=a.replace("()","")
 print("YES"if len(a)==0 else"NO")