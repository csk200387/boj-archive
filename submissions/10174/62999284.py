for i in[*open(0)][1::]:
 s=i.strip().lower()
 print('Yes'if s == s[::-1]else'No')