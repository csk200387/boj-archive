import re
inp = input()
if inp.find("_") != -1 :
    arr = re.findall("[^_]+", inp)
    str = arr[0]
    for i in range(1, len(arr)) :
        str += arr[i].title()
    print(str)
else :
    str = re.sub(r"(?<!^)(?=[A-Z])", "_", inp).lower()
    print(str)