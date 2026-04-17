arr = "WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./ 1234567890-="
trr = "QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,. `1234567890-"
print(*[trr[arr.index(i)] for i in input()], sep="")