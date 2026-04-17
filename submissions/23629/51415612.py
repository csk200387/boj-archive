import sys, re
input = lambda:sys.stdin.readline().rstrip()
st = input().replace("ZERO","0").replace("ONE","1").replace("TWO","2").replace("THREE","3").replace("FOUR","4").replace("FIVE","5").replace("SIX","6").replace("SEVEN","7").replace("EIGHT","8").replace("NINE","9").replace("x","*")[:-1]

if re.search("[\+\-\=\*\/]{2}",st) == None :
    try :
        a = str(int(eval(st)))
        res = a.replace("0","ZERO").replace("1","ONE").replace("2","TWO").replace("3","THREE").replace("4","FOUR").replace("5","FIVE").replace("6","SIX").replace("7","SEVEN").replace("8","EIGHT").replace("9","NINE")
        print(st.replace("*","x")+"=")
        print(res)
    except :
        print("Madness!")
else :
    print("Madness!")