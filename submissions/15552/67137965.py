import os, io
def main():
    print_ = print
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    for _ in range(int(input())):
        a,b=map(int,input().split())
        print_(a+b)

main()