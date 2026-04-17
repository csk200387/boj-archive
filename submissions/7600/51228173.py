import sys, collections
input = lambda:sys.stdin.readline().rstrip()
alphabet = "abcdefghijklmnopqrstuvwxyz"
dic = {}
while True :
    inp = input()
    if inp == "#" :
        break
    else :
        inp = inp.lower()
        for i in inp :
            if i in list(alphabet) :
                try :
                    dic[i] += 1
                except :
                    dic[i] = 1
            else :
                pass
        print(len(dic.keys()))