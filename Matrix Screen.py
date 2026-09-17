import random
import time
import os

chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

min_width = 20  
max_width = 120 

while True:
    width = random.randint(min_width, max_width)
    line = "".join(random.choice(chars) for _ in range(width))
    print("\033[92m" + line + "\033[0m")
    time.sleep(0.03)
