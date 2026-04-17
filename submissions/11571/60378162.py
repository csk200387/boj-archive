def fraction_to_decimal(un: int, dn: int) -> str:
    if un == 0:
        return "0"
    sign = "-" if un * dn < 0 else ""
    un, dn = abs(un), abs(dn)
    intg = un // dn
    un %= dn
    if un == 0:
        return sign + str(intg)
    decimal = []
    tmp = {}
    iss = False
    while un > 0 and not iss:
        un *= 10
        qu, un = divmod(un, dn)
        decimal.append(str(qu))
        if un in tmp:
            start = tmp[un]
            decimal.insert(start, "(")
            decimal.append(")")
            iss = True
        else:
            tmp[un] = len(decimal)
    rstr = "".join(decimal)
    return sign + str(intg) + "." + rstr

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(fraction_to_decimal(a, b))