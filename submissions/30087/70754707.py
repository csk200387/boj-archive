n,*t=open(0)
for i in t:
 match i[3]:
  case'o':m=204
  case'a':m=207
  case'i':m=302
  case'e':m='B101'
  case'w':m=303
  case'r':m=501
  case't':m=105
 print(m)