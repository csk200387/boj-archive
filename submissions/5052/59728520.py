for i in range(int(input())):
 s=[input()for j in range(int(input()))]
 s.sort()
 for j in range(1,len(s)):
  if s[j-1]==s[j][:len(s[j-1])]:
   print("NO")
   break
 else:print("YES")