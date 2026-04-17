import re
print("I love UCPC" if re.sub("[^A-Z]", "", input()) == "UCPC" else "I hate UCPC")