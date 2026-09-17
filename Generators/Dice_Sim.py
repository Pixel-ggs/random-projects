import random
import time
import os

def checks():
    if cur[c-1] == num[c-1]:
        num[c-1] = random.randint(1, 6)
        checks()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        if dn == 1:
            print("\n\033[94mDice Sim!!\033[0m\n\n","\t",num[0],"\n\n")
        else:
            print("\n\033[94mDice Sim!!\033[0m\n\n")
            for h in range(dn):
                print("\t",num[h],"\n\n")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    dn = int(input("\033[31m\nNumber of dice: \033[0m"))
    fin = []

    for i in range(dn):
        i = random.randint(1, 6)
        fin.append(i)

    cur = []

    for c in range(dn):
        c = 0
        cur.append(c)

    q = 0
    t = 0.05

    while True:
        num = []

        for n in range(dn):
            n = random.randint(1, 6)
            num.append(n)

        for c in range(dn):
            checks()
        
        for r in range(dn):
            cur[r-1] = num[r-1]

        time.sleep(t)
        q += 0.005
        t += q
        if t >= 0.5:
            break

    os.system('cls' if os.name == 'nt' else 'clear')

    if dn == 1:
        print("\n\033[31mRoll:\033[0m\n\n","\t",fin[0],"\n\n")
    else:
        print("\n\033[31mRolls:\033[0m\n")
        for p in range(dn):
            print("\t",fin[p],"\n\n")

    input("Press enter to continue: ")
    time.sleep(0.5)
