import sys
input = sys.stdin.readline
div = int(input())
while True :
    tmp = int(input())
    if tmp == 0 :
        break
    else :
        if tmp % div == 0 :
            print(f"{tmp} is a multiple of {div}.")
        else :
            print(f"{tmp} is NOT a multiple of {div}.")