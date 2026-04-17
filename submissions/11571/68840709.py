def fraction_to_decimal(N, M):
    result = []

    if (N < 0) ^ (M < 0):
        result.append("-")

    N, M = abs(N), abs(M)

    result.append(str(N//M))
    rmd = N%M

    if rmd == 0:
        return "".join(result)

    result.append(".")

    seen_rmds = {}
    while rmd != 0:
        if rmd in seen_rmds:
            nrp = result[:seen_rmds[rmd]]
            rp = result[seen_rmds[rmd]:]
            return "".join(nrp) + "(" + "".join(rp) + ")"

        seen_rmds[rmd] = len(result)
        rmd *= 10
        result.append(str(rmd // M))
        rmd %= M

    return "".join(result)

for i in range(int(input())):
    N, M = map(int, input().split())
    result = fraction_to_decimal(N, M)
    if "." not in result:
        result += ".(0)"
    elif "(" not in result:
        result += "(0)"
    print(result)