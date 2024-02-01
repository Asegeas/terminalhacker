from rich.console import Console
import random
import json
import time
import sys

def slowPrint(string, speed=0.05):
    loop = 0
    for char in string:
        try:
            if f"{char}{string[string.index(char) + 1]}" == "\n":
                loop += 1
                console.print("\n")
        except:
            console.print(f"{char}", style="rgb(32,194,14)", end='') # Print out the hacker text in hacker green
            sys.stdout.flush()
            time.sleep(speed)
        if loop == 1:
            loop -= 1
        else:
            console.print(f"{char}", style="rgb(32,194,14)", end='') # Print out the hacker text in hacker green
            sys.stdout.flush()
            time.sleep(speed)

console = Console()


def main():
    count = 0 # variable for controlling the loops of while 
    # enter the length of your hacker coding session

    console.print("You are accessing the mainframe.. continue(y/n):")
    duter = input("") # takes a number
    with open("scripts.JSON", 'r') as scpt:
        object = json.load(scpt)
    try:
        duter = int(duter)

    except:
        duter = 64 # default value of 'duter' if user enters non numerical units
    while count <= duter:
        rnd = random.randrange(0, 7)
        count += 1
        put = object['initialHC'][rnd]
        slowPrint(put, 0.01) # Print out slowly from here: https://stackoverflow.com/questions/66913084/print-slowly-in-terminal-python
        rnd2 = random.randrange(0, 7)
        put2 = object['secondaryHC'][rnd2]
        slowPrint(put2, 0.01) # Print out the hacker text in hacker green

if __name__ == '__main__':
    main()