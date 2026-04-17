a,*arr=open(0)
t=sorted(arr)
print("INCREASING"if t==arr else"DECREASING"if t[::-1]==arr else"NEITHER")