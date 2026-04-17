from sys import stdin, stdout
def main():
    p = stdout.write
    i = stdin.readline
    num = int(i())
    p(str("".join([str(i) for i in range(1,num+1)]).find(str(num))+1))

main()