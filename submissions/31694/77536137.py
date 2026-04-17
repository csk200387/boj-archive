def solve():

    a = list(map(int, input().split()))

    b = list(map(int, input().split()))

    c = sum(a)

    d = sum(b)

    if c != d:

        print("Algosia" if c > d else "Bajtek")

        return

    for i in range(10, 0, -1):

        e = a.count(i)

        f = b.count(i)

        if e != f:

            print("Algosia" if e > f else "Bajtek")

            return

    print("remis")

if __name__ == "__main__":

    solve()