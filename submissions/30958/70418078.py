from collections import Counter
input()
d = Counter(input()).most_common()
i = 0
while not d[i][0].isalpha():i+=1
print(d[i][1])