import random
import string
import time

LET = string.ascii_letters
DIG = string.digits
SYM = string.punctuation
ALL = LET + DIG + SYM

while True:
    LEN = int(input("\033[92mEnter the length of the password: \033[0m"))
    FIN = "".join(random.choice(ALL) for i in range(LEN))
    print(f"\033[95m{FIN}\033[0m")
    time.sleep(3)
