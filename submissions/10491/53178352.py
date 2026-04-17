import sys
for L in sys.stdin :
    if "problem" in L.lower() :
        print("yes")
    else :
        print("no")