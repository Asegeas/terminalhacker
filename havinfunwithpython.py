from rich.console import Console
import random
console = Console()

def main():
    count = 0 # variable for controlling the loops of while 
    # enter the length of your hacker coding session

    console.print("You are accessing the mainframe.. continue(y/n):")
    duter = input("") # takes a number

    try:
        duter = int(duter)

    except:
        duter = 64 # default value of 'duter' if user enters non numerical units
    while count <= duter:
        random.randrange(0, 4)
        count += 1
        console.print(f"{thing}", style="rgb(32,194,14)")

if __name__ == '__main__':
    main()