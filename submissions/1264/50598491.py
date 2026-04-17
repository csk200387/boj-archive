while True :
    a = input().lower().replace(" ","")
    if a == "#" :
        break
    else :
        print(len(a)-len(a.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")))