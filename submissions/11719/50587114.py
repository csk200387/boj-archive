import sys
while True:
    try:
        print(sys.stdin.readline().rstrip("\n"))
    except EOFError:
        break