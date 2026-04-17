R={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000};
for _ in range(int(input())):n=input();a=[R[c]for c in n];print(sum([-x if x<y else x for x,y in zip(a,a[1:]+[0])]))