def main():
    print_ = print
    n = int(input())
    arr = [0]*(n+2)
    arr[1], arr[2] = 1, 2
    for i in range(3, n+1):
        arr[i] = (arr[i-1] + arr[i-2]) % 10007
    print_(arr[n])
main()