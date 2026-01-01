import time
import os

RED = "\033[91m"
RESET = "\033[0m"

logo = [
"███╗   ██╗███████╗████████╗███████╗██╗     ██╗██╗  ██╗",
"████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║     ██║╚██╗██╔╝",
"██╔██╗ ██║█████╗     ██║   █████╗  ██║     ██║ ╚███╔╝ ",
"██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║     ██║ ██╔██╗ ",
"██║ ╚████║███████╗   ██║   ██║     ███████╗██║██╔╝ ██╗",
"╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝╚═╝  ╚═╝"
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def netflix_logo():
    clear()
    for line in logo:
        print(RED + line + RESET)
        time.sleep(0.15)

netflix_logo()

print("**this program recommend a series to you and you should see the recommended series** \n")


def recommended(series):
    print("~ you might like" , series)

def main():

    choose = int(input("choose between 1 to 5 : \n"))

    if choose == 2 :
        recommended("****dexter****")

    elif choose == 3:
        recommended("**maid**")

    elif choose == 1:
        recommended("***punisher***")

    elif choose == 4:
            recommended("***star wars***")

    elif choose == 5:
            recommended("***stranger things***")
    else :
         print(" your number must be between 1 to 5 \t")

main()