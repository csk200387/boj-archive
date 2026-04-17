for i in range(int(input())):
 h,m,s=map(lambda x:f"{int(x):06b}",input().split(':'))
 print("".join(["".join(x)for x in zip(h,m,s)]),h+m+s)