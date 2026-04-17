import sys


max = -1e7

tmp = ""
while True:
    read = sys.stdin.read(1)
    if read == "\n":
        if max <= int(tmp):
            max = int(tmp)
        else:
            print("Bad")
            exit()
        break

    if read == " ":
        if max <= int(tmp):
            max = int(tmp)
        else:
            print("Bad")
            exit()
        tmp = ""
    else:
        tmp += read

print("Good")