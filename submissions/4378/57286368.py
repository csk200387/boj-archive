arr = "WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./ "
trr = "QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,. "
print(*[trr[arr.index(i)] for i in input()], sep="")