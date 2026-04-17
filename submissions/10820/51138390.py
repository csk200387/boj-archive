import re, sys
input = lambda:sys.stdin.readline().rstrip()
c1 = re.compile('[a-z]')
c2 = re.compile('[A-Z]')
c3 = re.compile('[0-9]')
c4 = re.compile('[\s]')
while 1:
    try:
        str = input()
        r1 = len(re.findall(c1, str))
        r2 = len(re.findall(c2, str))
        r3 = len(re.findall(c3, str))
        r4 = len(re.findall(c4, str))
        print(r1, r2, r3, r4)
    except EOFError:
        break