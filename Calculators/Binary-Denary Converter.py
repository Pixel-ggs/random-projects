'''
Number system converter between binary and denary
Used Copilot to simplify and cleanup code a bit but the actual stuff was by me

'''

# importing modules
import os, subprocess

# defining variables
start_base = int(input("\nFor \033[32mBinary\033[0m -> \033[36mDenary\033[0m, enter 1.\n\nFor \033[36mDenary\033[0m -> \033[32mBinary\033[0m, enter 0.\n\n"))
remainders = []
values = []

# binary -> denary conversion
if start_base == 1:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

    start_num = input("\nEnter the \033[32mbinary\033[0m number. (e.g. '01000011')\n\n")
    digits = list(start_num)[::-1]
    total = 0

    for i in range(len(digits)):

        # invalid input
        if digits[i] not in ("0", "1"):
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal
            print("\033[31mInvalid input\033[0m")
            break

        # generating the denary
        total += int(digits[i]) * (2 ** i)
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

    # final output
    print(f"\n\033[36mDenary\033[0m equivalent of \033[33m{start_num}\033[0m:\n\n\033[33m{total}\033[0m\n")

# denary -> binary conversion
elif start_base == 0:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

    start_num = int(input("\nEnter the \033[36mdenary\033[0m number. (e.g. \'135')\n\n"))
    division = start_num

    while True:

        # final output
        if division < 1:
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal

            remainders.reverse()
            final_binary = "".join(remainders)
            print(f"\n\033[32mBinary\033[0m equivalent of \033[33m{start_num}\033[0m:\n\n\033[33m{final_binary}\033[0m\n")

            break # stop code

        # generating the binary
        else: 
            division, remainder = divmod(division, 2)
            remainders.append(str(remainder))

# invalid input
else:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # clear terminal
    print("\n\033[31mInvalid Input\033[0m\n")

input("\nPress enter to exit\n\n")
