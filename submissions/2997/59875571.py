a,b,c=sorted(map(int,input().split()))
print(c*2-b if a==b==c else b*2-c if b-a>c-b else b*2-a)