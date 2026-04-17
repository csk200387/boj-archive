import sys
arr = "WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./ 1234567890-=\n"
trr = "QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,. `1234567890-\n"
for l in sys.stdin :
    print(*[trr[arr.index(i)] for i in l], sep="", end="")