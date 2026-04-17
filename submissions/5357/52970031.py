import re
for i in range(int(input())) :
    print(re.sub('([A-Z])\\1*','\\1',input()))