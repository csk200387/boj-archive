import os
pidnum = os.getpid()
with open(f"/proc/{pidnum}/fd/1", "r") as input:
    print(input.read(), end="")