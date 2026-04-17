import re
print("cute" if re.fullmatch(".*driip$", input()) != None else "not cute")