inputNum = int(input("")) 
def score(n):
    if  90 <= n : return "A"
    elif 80 <= n : return "B"
    elif 70 <= n : return "C"
    elif 60 <= n : return "D"
    else : return "F"
print(score(inputNum))