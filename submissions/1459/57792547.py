x,y,w,s=map(int,input().split());t=max(x,y);y=min(x,y)
print(min((x+y)*w,min((t-1)*s+w,t*s),y*s + abs(x-y)*w))